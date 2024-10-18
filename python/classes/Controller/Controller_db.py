from Mongodb_class.Mongo_connect import MongoDBConnection
from classes import Role, User, AuditLog, Budget, Category, Period, Notification, Expense, Report, KPI, Project, Revenue

class DataManager:
    def __init__(self, uri, db_name):
        self.mongo_connection = MongoDBConnection(uri, db_name)

    def load_roles(self):
        collection = self.mongo_connection.get_collection("roles")
        roles_data = collection.find()  # Charge tous les rôles
        roles = [Role(role['role_id'], role['role_name']) for role in roles_data]
        return roles

    def load_users(self):
        collection = self.mongo_connection.get_collection("users")
        users_data = collection.find()  # Charge tous les utilisateurs
        users = [User(user['user_id'], user['first_name'], user['last_name'], user['email'], user['password_hash'], user['role']) for user in users_data]
        return users

    def load_audit_logs(self):
        collection = self.mongo_connection.get_collection("audit_logs")
        logs_data = collection.find()  # Charge tous les logs
        audit_logs = [AuditLog(log['log_id'], log['user'], log['action'], log['timestamp']) for log in logs_data]
        return audit_logs

    def load_budgets(self):
        collection = self.mongo_connection.get_collection("budgets")
        budgets_data = collection.find()  # Charge tous les budgets
        budgets = [Budget(budget['budget_id'], budget['amount'], budget['start_date'], budget['end_date'], budget['category'], budget['project']) for budget in budgets_data]
        return budgets

    def load_categories(self):
        collection = self.mongo_connection.get_collection("categories")
        categories_data = collection.find()  # Charge toutes les catégories
        categories = [Category(category['category_id'], category['category_name']) for category in categories_data]
        return categories

    def load_periods(self):
        collection = self.mongo_connection.get_collection("periods")
        periods_data = collection.find()  # Charge toutes les périodes
        periods = [Period(period['period_id'], period['start_date'], period['end_date']) for period in periods_data]
        return periods

    def load_notifications(self):
        collection = self.mongo_connection.get_collection("notifications")
        notifications_data = collection.find()  # Charge toutes les notifications
        notifications = [Notification(notification['notification_id'], notification['user'], notification['message'], notification['status'], notification['created_at']) for notification in notifications_data]
        return notifications

    def load_expenses(self):
        collection = self.mongo_connection.get_collection("expenses")
        expenses_data = collection.find()  # Charge toutes les dépenses
        expenses = [Expense(expense['expense_id'], expense['description'], expense['amount'], expense['date'], expense['category'], expense['project'], expense['created_by']) for expense in expenses_data]
        return expenses

    def load_reports(self):
        collection = self.mongo_connection.get_collection("reports")
        reports_data = collection.find()  # Charge tous les rapports
        reports = [Report(report['report_id'], report['report_type'], report['generated_at'], report['period'], report['created_by']) for report in reports_data]
        return reports

    def load_kpis(self):
        collection = self.mongo_connection.get_collection("kpis")
        kpis_data = collection.find()  # Charge tous les KPIs
        kpis = [KPI(kpi['kpi_id'], kpi['name'], kpi['value'], kpi['date']) for kpi in kpis_data]
        return kpis

    def load_projects(self):
        collection = self.mongo_connection.get_collection("projects")
        projects_data = collection.find()  # Charge tous les projets
        projects = [Project(project['project_id'], project['project_name'], project['start_date'], project['end_date'], project['created_by']) for project in projects_data]
        return projects

    def load_revenues(self):
        collection = self.mongo_connection.get_collection("revenues")
        revenues_data = collection.find()  # Charge tous les revenus
        revenues = [Revenue(revenue['revenue_id'], revenue['description'], revenue['amount'], revenue['date'], revenue['period'], revenue['created_by']) for revenue in revenues_data]
        return revenues

    def close(self):
        self.mongo_connection.close_connection()

# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez par vos informations d'identification et votre URI MongoDB
    username = "your_username"
    password = "your_password"
    host = "localhost"
    port = "27017"
    database_name = "mydatabase"
    mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/{database_name}"

    data_manager = DataManager(mongo_uri, database_name)

    # Chargement des données
    roles = data_manager.load_roles()
    users = data_manager.load_users()
    audit_logs = data_manager.load_audit_logs()
    budgets = data_manager.load_budgets()
    categories = data_manager.load_categories()
    periods = data_manager.load_periods()
    notifications = data_manager.load_notifications()
    expenses = data_manager.load_expenses()
    reports = data_manager.load_reports()
    kpis = data_manager.load_kpis()
    projects = data_manager.load_projects()
    revenues = data_manager.load_revenues()

    # Fermer la connexion
    data_manager.close()
