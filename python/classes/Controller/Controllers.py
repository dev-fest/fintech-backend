from Mongodb_class.Mongo_connect import MongoDBConnection
from classes import Role, User, AuditLog, Budget, Category, Period, Notification, Expense, Report, KPI, Project, Revenue
from subject import Subject

class UserController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("users")


    def add(self, user):
        self.collection.insert_one(user.__dict__)
        self.notify_observers(f"users")


    def delete(self, user_id):
        self.collection.delete_one({"user_id": user_id})
        self.notify_observers(f"users")

    def update(self, user_id, updated_data):
        self.collection.update_one({"user_id": user_id}, {"$set": updated_data})
        self.notify_observers(f"users")

    def search(self, **kwargs):
        users_data = self.collection.find(kwargs)
        return [User(user['user_id'], user['first_name'], user['last_name'], user['email'], user['password_hash'], user['role']) for user in users_data]


class RoleController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("roles")

    def add(self, role):
        self.collection.insert_one(role.__dict__)
        self.notify_observers(f"role")

    def delete(self, role_id):
        self.collection.delete_one({"role_id": role_id})
        self.notify_observers(f"role")

    def update(self, role_id, updated_data):
        self.collection.update_one({"role_id": role_id}, {"$set": updated_data})
        self.notify_observers(f"role")

    def search(self, **kwargs):
        roles_data = self.collection.find(kwargs)
        return [Role(role['role_id'], role['role_name']) for role in roles_data]


class BudgetController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("budgets")

    def add(self, budget):
        self.collection.insert_one(budget.__dict__)
        self.notify_observers(f"budget")

    def delete(self, budget_id):
        self.collection.delete_one({"budget_id": budget_id})
        self.notify_observers(f"budget")

    def update(self, budget_id, updated_data):
        self.collection.update_one({"budget_id": budget_id}, {"$set": updated_data})
        self.notify_observers(f"budget")

    def search(self, **kwargs):
        budgets_data = self.collection.find(kwargs)
        return [Budget(budget['budget_id'], budget['amount'], budget['start_date'], budget['end_date'], budget['category'], budget['project']) for budget in budgets_data]

class AuditLogController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("audit_logs")

    def add(self, audit_log):
        self.collection.insert_one(audit_log.__dict__)
        self.notify_observers(f"audit_log")

    def delete(self, log_id):
        self.collection.delete_one({"log_id": log_id})
        self.notify_observers(f"audit_log")

    def update(self, log_id, updated_data):
        self.collection.update_one({"log_id": log_id}, {"$set": updated_data})
        self.notify_observers(f"audit_log")

    def search(self, **kwargs):
        logs_data = self.collection.find(kwargs)
        return [AuditLog(log['log_id'], log['user'], log['action'], log['timestamp']) for log in logs_data]


class CategoryController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("categories")

    def add(self, categorie):
        self.collection.insert_one(categorie.__dict__)
        self.notify_observers(f"categorie")

    def delete(self, category_id):
        self.collection.delete_one({"category_id": category_id})
        self.notify_observers(f"categorie")

    def update(self, category_id, updated_data):
        self.collection.update_one({"category_id": category_id}, {"$set": updated_data})
        self.notify_observers(f"categorie")

    def search(self, **kwargs):
        categories_data = self.collection.find(kwargs)
        return [Category(category['category_id'], category['category_name']) for category in categories_data]
        

class PeriodController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("periods")

    def add(self, period):
        self.collection.insert_one(period.__dict__)
        self.notify_observers(f"period")

    def delete(self, period_id):
        self.collection.delete_one({"period_id": period_id})
        self.notify_observers(f"period")

    def update(self, period_id, updated_data):
        self.collection.update_one({"period_id": period_id}, {"$set": updated_data})
        self.notify_observers(f"period")

    def search(self, **kwargs):
        periods_data = self.collection.find(kwargs)
        return [Period(period['period_id'], period['start_date'], period['end_date']) for period in periods_data]
    

class NotificationController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("notifications")

    def add(self, notification):
        self.collection.insert_one(notification.__dict__)
        self.notify_observers(f"notification")

    def delete(self, notification_id):
        self.collection.delete_one({"notification_id": notification_id})
        self.notify_observers(f"notification")

    def update(self, notification_id, updated_data):
        self.collection.update_one({"notification_id": notification_id}, {"$set": updated_data})
        self.notify_observers(f"notification")

    def search(self, **kwargs):
        notifications_data = self.collection.find(kwargs)
        return [Notification(notification['notification_id'], notification['user'], notification['message'], notification['status'], notification['created_at']) for notification in notifications_data]
        

class ExpenseController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("expenses")

    def add(self, expense):
        self.collection.insert_one(expense.__dict__)
        self.notify_observers(f"expense")

    def delete(self, expense_id):
        self.collection.delete_one({"expense_id": expense_id})
        self.notify_observers(f"expense")

    def update(self, expense_id, updated_data):
        self.collection.update_one({"expense_id": expense_id}, {"$set": updated_data})
        self.notify_observers(f"expense")

    def search(self, **kwargs):
        expenses_data = self.collection.find(kwargs)
        return [Expense(expense['expense_id'], expense['description'], expense['amount'], expense['date'], expense['category'], expense['project'], expense['created_by']) for expense in expenses_data]
        

class ReportController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("reports")

    def add(self, report):
        self.collection.insert_one(report.__dict__)
        self.notify_observers(f"report")

    def delete(self, report_id):
        self.collection.delete_one({"report_id": report_id})
        self.notify_observers(f"report")

    def update(self, report_id, updated_data):
        self.collection.update_one({"report_id": report_id}, {"$set": updated_data})
        self.notify_observers(f"report")

    def search(self, **kwargs):
        reports_data = self.collection.find(kwargs)
        return [Report(report['report_id'], report['report_type'], report['generated_at'], report['period'], report['created_by']) for report in reports_data]
       
        
class RevenueController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("revenues")

    def add(self, revenue):
        self.collection.insert_one(revenue.__dict__)
        self.notify_observers(f"revenue")

    def delete(self, revenue_id):
        self.collection.delete_one({"revenue_id": revenue_id})
        self.notify_observers(f"revenue")

    def update(self, revenue_id, updated_data):
        self.collection.update_one({"revenue_id": revenue_id}, {"$set": updated_data})
        self.notify_observers(f"revenue")

    def search(self, **kwargs):
        revenues_data = self.collection.find(kwargs)
        return [Revenue(revenue['revenue_id'], revenue['description'], revenue['amount'], revenue['date'], revenue['period'], revenue['created_by']) for revenue in revenues_data]


class KPIController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("kpis")

    def add(self, kpi):
        self.collection.insert_one(kpi.__dict__)
        self.notify_observers(f"kpi")

    def delete(self, kpi_id):
        self.collection.delete_one({"kpi_id": kpi_id})
        self.notify_observers(f"kpi")

    def update(self, kpi_id, updated_data):
        self.collection.update_one({"kpi_id": kpi_id}, {"$set": updated_data})
        self.notify_observers(f"kpi")

    def search(self, **kwargs):
        kpis_data = self.collection.find(kwargs)
        return [KPI(kpi['kpi_id'], kpi['name'], kpi['value'], kpi['date']) for kpi in kpis_data]

class ProjectController(Subject):
    def __init__(self, db_connection):
        super().__init__()
        self.collection = db_connection.get_collection("projects")

    def add(self, project):
        self.collection.insert_one(project.__dict__)
        self.notify_observers(f"project")

    def delete(self, project_id):
        self.collection.delete_one({"project_id": project_id})
        self.notify_observers(f"project")

    def update(self, project_id, updated_data):
        self.collection.update_one({"project_id": project_id}, {"$set": updated_data})
        self.notify_observers(f"project")

    def search(self, **kwargs):
        projects_data = self.collection.find(kwargs)
        return  [Project(project['project_id'], project['project_name'], project['start_date'], project['end_date'], project['created_by']) for project in projects_data]