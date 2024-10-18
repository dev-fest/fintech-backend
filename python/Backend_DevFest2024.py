from Mongodb_class.Mongo_connect import MongoDBConnection



# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez par vos informations d'identification et votre URI MongoDB
    username = "your_username"
    password = "your_password"
    host = "localhost"
    port = "27017"
    database_name = "mydatabase"
    mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/{database_name}"

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
