from Mongodb_class.Mongo_connect import MongoDBConnection
from classes.Controller.Controllers import UserController
from classes.Controller.observer import ConcreteObserver


def connect(mongo_uri, database_name) :
    mongo_connection = MongoDBConnection(mongo_uri, database_name)

    # Utilisation des contrôleurs
    user_controller = UserController(mongo_connection)
    role_controller = RoleController(mongo_connection)
    budget_controller = BudgetController(mongo_connection)

    # Ajout d'un utilisateur
    new_user = User("u001", "John", "Doe", "john.doe@example.com", "hashed_password", "role_id_1")
    user_controller.add(new_user)

    # Recherche d'utilisateurs
    users = user_controller.search(first_name="John")
    print(users)

    # Mise à jour d'un rôle
    role_controller.update("role_id_1", {"role_name": "Administrator"})

    # Suppression d'un budget
    budget_controller.delete("budget_id_1")

    # Fermer la connexion
    mongo_connection.close_connection()




# Ajout d’un observateur
observer = ConcreteObserver()
user_controller.add_observer(observer)

# Ajout d’un utilisateur
new_user = User("u001", "John", "Doe", "john.doe@example.com", "hashed_password", "role_id_1")
user_controller.add(new_user)

# Modification d’un utilisateur
user_controller.update("u001", {"first_name": "Johnny"})

# Suppression d’un utilisateur
user_controller.delete("u001")
