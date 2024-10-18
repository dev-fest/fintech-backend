from Mongodb_class.Mongo_connect import MongoDBConnection
from classes.Controller.Controllers import RoleController, UserController, AuditLogController, BudgetController, CategoryController, PeriodController, NotificationController, ExpenseController, ReportController, KPIController, ProjectController, RevenueController
from classes.Controller.observer import ConcreteObserver
from classes.Report import Report
from classes.Revenue import Revenue

# Assurez-vous de remplacer "your_module_name" et "your_model_module" par les noms réels de vos modules.

# Initialisation de la connexion à la base de données MongoDB
db_connection = MongoDBConnection()


revenue_controller = RevenueController(db_connection)
user_controller = UserController(db_connection)
audit_log_controller = AuditLogController(db_connection)
budget_controller = BudgetController(db_connection)
category_controller = CategoryController(db_connection)
period_controller = PeriodController(db_connection)
notification_controller = NotificationController(db_connection)
expense_controller = ExpenseController(db_connection)
report_controller = ReportController(db_connection)
kpi_controller = KPIController(db_connection)
project_controller = ProjectController(db_connection)
role_controller = RoleController(db_connection)


def add_revenue(description, amount, date, period, created_by):
    """Ajoute un revenu à la base de données."""
    revenue = Revenue(revenue_id=None, description=description, amount=amount, date=date, period=period, created_by=created_by)
    revenue_controller.add(revenue)
    print(f"Revenu ajouté: {description}")

def delete_revenue(revenue_id):
    """Supprime un revenu par son ID."""
    revenue_controller.delete(revenue_id)
    print(f"Revenu avec ID {revenue_id} supprimé.")

def update_revenue(revenue_id, updated_data):
    """Met à jour un revenu par son ID."""
    revenue_controller.update(revenue_id, updated_data)
    print(f"Revenu avec ID {revenue_id} mis à jour.")

def search_revenues(**kwargs):
    """Recherche des revenus selon les critères donnés."""
    results = revenue_controller.search(**kwargs)
    return results

report_controller = ReportController(db_connection)

def add_report(report_type, generated_at, period, created_by):
    """Ajoute un rapport à la base de données."""
    report = Report(report_id=None, report_type=report_type, generated_at=generated_at, period=period, created_by=created_by)
    report_controller.add(report)
    print(f"Rapport ajouté: {report_type}")

def delete_report(report_id):
    """Supprime un rapport par son ID."""
    report_controller.delete(report_id)
    print(f"Rapport avec ID {report_id} supprimé.")

def update_report(report_id, updated_data):
    """Met à jour un rapport par son ID."""
    report_controller.update(report_id, updated_data)
    print(f"Rapport avec ID {report_id} mis à jour.")

def search_reports(**kwargs):
    """Recherche des rapports selon les critères donnés."""
    results = report_controller.search(**kwargs)
    return results
