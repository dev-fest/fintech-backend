from datetime import datetime, timedelta
import bcrypt
import jwt
from dotenv import load_dotenv  # Importer la fonction load_dotenv
import os
from bson.objectid import ObjectId
from classes.Controller.subject import Subject
from threading import Lock
from abc import ABC, abstractmethod

# Charger les variables depuis le fichier .env
load_dotenv()

# Récupérer les clés secrètes
SECRET_KEY = os.getenv("SECRET_KEY")
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")

refresh_tokens_store = {}  # Stocker les refresh tokens en mémoire (à adapter avec une base)

class BaseController(Subject, ABC):
    """Classe mère pour les contrôleurs avec Singleton et gestion MongoDB."""
    _instance = None
    _lock = Lock()

    def __new__(cls, db_connection, *args, **kwargs):
        """Singleton avec verrouillage."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(BaseController, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_connection, collection_name):
        """Initialise la collection MongoDB."""
        if not hasattr(self, '_initialized'):
            super().__init__()
            self.collection = db_connection.get_collection(collection_name)
            self._initialized = True

    def add(self, document):
        """Ajoute un document à la collection."""
        if isinstance(document, list):
            self.collection.insert_many(document)
        else:
            self.collection.insert_one(document)
        self.notify_observers(f"{self.__class__.__name__}: ajout")

    def delete(self, document_id):
        """Supprime un document par son ID."""
        if isinstance(document_id, str):
            document_id = ObjectId(document_id)
        self.collection.delete_one({"_id": document_id})
        self.notify_observers(f"{self.__class__.__name__}: suppression")

    def update(self, document_id, updated_data):
        """Met à jour un document par son ID."""
        if isinstance(document_id, str):
            document_id = ObjectId(document_id)
        self.collection.update_one({"_id": document_id}, {"$set": updated_data})
        self.notify_observers(f"{self.__class__.__name__}: mise à jour")

    def get_all(self):
        """Récupère tous les documents de la collection."""
        documents = self.collection.find()
        return [self._convert_object_id(doc) for doc in documents]

    def _convert_object_id(self, doc):
        """Convertit l'ObjectId en string."""
        doc['_id'] = str(doc['_id'])
        return doc

    @abstractmethod
    def search(self, **kwargs):
        """Méthode de recherche à implémenter par les classes enfants."""
        pass


class UserController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "users")

    def add(self, document):
        """Ajoute un utilisateur en hachant son mot de passe."""
        if isinstance(document, list):
            for doc in document:
                doc['password'] = self._hash_password(doc['password'])
        else:
            document['password'] = self._hash_password(document['password'])

        super().add(document)

    def _hash_password(self, password):
        """Hache le mot de passe avec bcrypt."""
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')

    def search(self, **kwargs):
        users_data = self.collection.find(kwargs)
        return [
            {
                '_id': str(user['_id']),
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'email': user['email'],
                'password': user['password'],
                'role_id': str(user['role_id'])
            }
            for user in users_data
        ]


    def authenticate(self, email, password):
        """Authentifie un utilisateur et renvoie les tokens JWT."""
        user = self.collection.find_one({'email': email})

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            # Générer les tokens JWT
            access_token = self._generate_access_token(user['_id'],user['first_name'],user['last_name'],user['email'],user['password'],user['role_id'])
            refresh_token = self._generate_refresh_token(user['_id'], user['role_id'])

            user['access_token'] = access_token
            user['refresh_token'] = refresh_token
            # Stocker le refresh token
            refresh_tokens_store[str(user['_id']), str(user['role_id'])] = refresh_token
            return {
                'message': 'Connexion réussie',
                'access_token': access_token
                #'refresh_token': refresh_token
            }

        return {'error': 'Email ou mot de passe incorrect'}


    def _generate_access_token(self, user_id,first_name,last_name,email,password,role_id):
            """Génère un token JWT valide pendant 24 heure."""
            payload = {
                'user_id': str(user_id),
                'first_name': str(first_name),
                'last_name': str(last_name),
                'email': str(email),
                'password': str(password),
                'role_id': str(role_id),
                'exp': datetime.utcnow() + timedelta(hours=24)
            }
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    def _generate_refresh_token(self, user_id, role_id, expires_in=7):
        """Génère un refresh token valide pour 7 jours."""
        payload = {
            'user_id': str(user_id),
            'role_id': str(role_id),
            'exp': datetime.utcnow() + timedelta(days=expires_in)
        }
        return jwt.encode(payload, REFRESH_SECRET_KEY, algorithm='HS256')

    def refresh_access_token(self, refresh_token):
        """Rafraîchit l'access token avec un refresh token valide."""
        try:
            payload = jwt.decode(refresh_token, REFRESH_SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']

            # Vérifier si le refresh token est valide
            if refresh_tokens_store.get(user_id) != refresh_token:
                return {'error': 'Refresh token invalide'}, 401

            # Générer un nouveau access token
            new_access_token = self._generate_access_token(user_id, 'admin')  # Adapter le rôle si nécessaire
            return {'access_token': new_access_token}, 200

        except jwt.ExpiredSignatureError:
            return {'error': 'Refresh token expiré'}, 401
        except jwt.InvalidTokenError:
            return {'error': 'Refresh token invalide'}, 401

    def verify_token(self, token):
        """Vérifie le token JWT."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return {'valid': True, 'user_id': payload['user_id']}
        except jwt.ExpiredSignatureError:
            return {'valid': False, 'error': 'Token expiré'}
        except jwt.InvalidTokenError:
            return {'valid': False, 'error': 'Token invalide'}


class RoleController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "roles")
    
    def search(self, **kwargs):
        roles_data = self.collection.find(kwargs)
        return [
            {'_id': str(role['_id']), 'role_name': role['role_name']}
            for role in roles_data
        ]


class BudgetController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "budgets")

    def search(self, **kwargs):
        budgets_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(budget['_id']),
            'amount': budget['amount'],
            'start_date': budget['start_date'],
            'end_date': budget['end_date'],
            'category': budget['category'],
            'project': budget['project']
        }
        for budget in budgets_data
    ]

class AuditLogController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "audit_logs")

    def search(self, **kwargs):
        logs_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(log['_id']),
            'user': log['user'],
            'action': log['action'],
            'timestamp': log['timestamp']
        }
        for log in logs_data
    ]
        

class CategoryController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "categories")

    def search(self, **kwargs):
        categories_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(category['_id']),
            'category_name': category['category_name']
        }
        for category in categories_data
    ]

class PeriodController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "periods")

    def search(self, **kwargs):
        periods_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(period['_id']),
            'start_date': period['start_date'],
            'end_date': period['end_date']
        }
        for period in periods_data
    ]

class NotificationController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "notifications")


    def search(self, **kwargs):
        notifications_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(notification['_id']),
            'user': notification['user'],
            'message': notification['message'],
            'status': notification['status'],
            'created_at': notification['created_at']
        }
        for notification in notifications_data
    ]

class ExpenseController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "expenses")

    def search(self, **kwargs):
        expenses_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(expense['_id']),
            'description': expense['description'],
            'amount': expense['amount'],
            'date': expense['date'],
            'category': expense['category'],
            'project': expense['project'],
            'created_by': expense['created_by']
        }
        for expense in expenses_data
    ]

class ReportController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "reports")

    def search(self, **kwargs):
        """Recherche des rapports selon les critères donnés."""
        reports_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(report['_id']),
            'report_type': report['report_type'],
            'generated_at': report['generated_at'],
            'period': report['period'],
            'created_by': report['created_by']
        }
        for report in reports_data
    ]

class RevenueController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "revenues")

    def search(self, **kwargs):
        """Recherche des revenus selon les critères donnés."""
        revenues_data = self.collection.find(kwargs)
        return [
                {
                    '_id': str(revenue['_id']),
                    'description': revenue['description'],
                    'amount': revenue['amount'],
                    'date': revenue['date'],
                    'period': revenue['period'],
                    'created_by': revenue['created_by']
                }
                for revenue in revenues_data
            ]


class KPIController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "kpis")

    def search(self, **kwargs):
        kpis_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(kpi['_id']),
            'name': kpi['name'],
            'value': kpi['value'],
            'date': kpi['date']
        }
        for kpi in kpis_data
    ]
class ProjectController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "projects")

    def search(self, **kwargs):
        projects_data = self.collection.find(kwargs)
        return [
        {
            '_id': str(project['_id']),
            'project_name': project['project_name'],
            'start_date': project['start_date'],
            'end_date': project['end_date'],
            'created_by': project['created_by']
        }
        for project in projects_data
    ]