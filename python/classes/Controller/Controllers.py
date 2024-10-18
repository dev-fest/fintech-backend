from classes import Role, User, AuditLog, Budget, Category, Period, Notification, Expense, Report, KPI, Project, Revenue
from subject import Subject
from threading import Lock
from abc import ABC, abstractmethod

class BaseController(Subject, ABC):
    """Classe mère pour les contrôleurs avec Singleton et gestion MongoDB."""
    _instance = None
    _lock = Lock()  # Verrou pour multi-threading

    def __new__(cls, db_connection, *args, **kwargs):
        """Singleton avec verrouillage."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(BaseController, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_connection, collection_name):
        """Initialise la collection MongoDB."""
        if not hasattr(self, '_initialized'):  # Vérifie si l'instance est déjà initialisée
            super().__init__()
            self.collection = db_connection.get_collection(collection_name)
            self._initialized = True  # Marque comme initialisé

    def add(self, document):
        """Ajoute un document à la collection."""
        self.collection.insert_one(document.__dict__)
        self.notify_observers(f"{self.__class__.__name__}: ajout")

    def delete(self, document_id):
        """Supprime un document par son ID."""
        self.collection.delete_one({"_id": document_id})
        self.notify_observers(f"{self.__class__.__name__}: suppression")

    def update(self, document_id, updated_data):
        """Met à jour un document par son ID."""
        self.collection.update_one({"_id": document_id}, {"$set": updated_data})
        self.notify_observers(f"{self.__class__.__name__}: mise à jour")

    @abstractmethod
    def search(self, **kwargs):
        """Recherche dans la collection (méthode à implémenter par les classes enfants)."""
        pass



class UserController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "users")

    def search(self, **kwargs):
        users_data = self.collection.find(kwargs)
        return [User(user['user_id'], user['first_name'], user['last_name'], user['email'], user['password_hash'], user['role']) for user in users_data]


class RoleController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "roles")


    def search(self, **kwargs):
        roles_data = self.collection.find(kwargs)
        return [Role(role['role_id'], role['role_name']) for role in roles_data]


class BudgetController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "budgets")

    def search(self, **kwargs):
        budgets_data = self.collection.find(kwargs)
        return [Budget(budget['budget_id'], budget['amount'], budget['start_date'], budget['end_date'], budget['category'], budget['project']) for budget in budgets_data]

class AuditLogController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "audit_logs")

    def search(self, **kwargs):
        logs_data = self.collection.find(kwargs)
        return [AuditLog(log['log_id'], log['user'], log['action'], log['timestamp']) for log in logs_data]


class CategoryController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "categories")

    def search(self, **kwargs):
        categories_data = self.collection.find(kwargs)
        return [Category(category['category_id'], category['category_name']) for category in categories_data]
        

class PeriodController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "periods")

    def search(self, **kwargs):
        periods_data = self.collection.find(kwargs)
        return [Period(period['period_id'], period['start_date'], period['end_date']) for period in periods_data]
    

class NotificationController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "notifications")


    def search(self, **kwargs):
        notifications_data = self.collection.find(kwargs)
        return [Notification(notification['notification_id'], notification['user'], notification['message'], notification['status'], notification['created_at']) for notification in notifications_data]
        

class ExpenseController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "expenses")

    def search(self, **kwargs):
        expenses_data = self.collection.find(kwargs)
        return [Expense(expense['expense_id'], expense['description'], expense['amount'], expense['date'], expense['category'], expense['project'], expense['created_by']) for expense in expenses_data]
        
class ReportController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "reports")

    def search(self, **kwargs):
        """Recherche des rapports selon les critères donnés."""
        reports_data = self.collection.find(kwargs)
        return [
            Report(report['report_id'], report['report_type'], report['generated_at'], 
                   report['period'], report['created_by'])
            for report in reports_data
        ]

class RevenueController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "revenues")

    def search(self, **kwargs):
        """Recherche des revenus selon les critères donnés."""
        revenues_data = self.collection.find(kwargs)
        return [
            Revenue(revenue['revenue_id'], revenue['description'], revenue['amount'], 
                    revenue['date'], revenue['period'], revenue['created_by'])
            for revenue in revenues_data
        ]


class KPIController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "kpis")

    def search(self, **kwargs):
        kpis_data = self.collection.find(kwargs)
        return [KPI(kpi['kpi_id'], kpi['name'], kpi['value'], kpi['date']) for kpi in kpis_data]

class ProjectController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection, "projects")

    def search(self, **kwargs):
        projects_data = self.collection.find(kwargs)
        return  [Project(project['project_id'], project['project_name'], project['start_date'], project['end_date'], project['created_by']) for project in projects_data]