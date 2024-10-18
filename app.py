from flask import Flask, jsonify, request
from Mongodb_class.Mongo_connect import MongoDBConnection
from classes.Controller.Controllers import (
    RoleController, UserController, AuditLogController, BudgetController,
    CategoryController, PeriodController, NotificationController, ExpenseController,
    ReportController, KPIController, ProjectController, RevenueController
)

# Initialisation de Flask et de MongoDB
app = Flask(__name__)
uri = "mongodb+srv://greylanisteur123:CWihvdE3IHnEV3eK@cluster0.i4xu4.mongodb.net/"
my_db = "cluster0"
db_connection = MongoDBConnection(uri,my_db)

# Initialisation des contrôleurs
revenue_controller = RevenueController(db_connection)
report_controller = ReportController(db_connection)
role_controller = RoleController(db_connection)
# Ajoutez ici les autres contrôleurs si nécessaire.

### CRUD POUR REVENUE ###
@app.route('/role', methods=['POST'])
def add_role():
    data = request.json
    role_controller.add(data)
    return jsonify({"message": "Role ajouté avec succès"}), 201

### CRUD POUR REVENUE ###
@app.route('/revenues', methods=['POST'])
def add_revenue():
    data = request.json
    revenue_controller.add(data)
    return jsonify({"message": "Revenu ajouté avec succès"}), 201

@app.route('/revenues/<revenue_id>', methods=['DELETE'])
def delete_revenue(revenue_id):
    revenue_controller.delete(revenue_id)
    return jsonify({"message": f"Revenu avec ID {revenue_id} supprimé."}), 200

@app.route('/revenues/<revenue_id>', methods=['PUT'])
def update_revenue(revenue_id):
    data = request.json
    revenue_controller.update(revenue_id, data)
    return jsonify({"message": f"Revenu avec ID {revenue_id} mis à jour."}), 200

@app.route('/revenues', methods=['GET'])
def search_revenues():
    criteria = request.args.to_dict()
    results = revenue_controller.search(**criteria)
    return jsonify(results), 200


### CRUD POUR REPORT ###
@app.route('/reports', methods=['POST'])
def add_report():
    data = request.json
    report_controller.add(data)
    return jsonify({"message": "Rapport ajouté avec succès"}), 201

@app.route('/reports/<report_id>', methods=['DELETE'])
def delete_report(report_id):
    report_controller.delete(report_id)
    return jsonify({"message": f"Rapport avec ID {report_id} supprimé."}), 200

@app.route('/reports/<report_id>', methods=['PUT'])
def update_report(report_id):
    data = request.json
    report_controller.update(report_id, data)
    return jsonify({"message": f"Rapport avec ID {report_id} mis à jour."}), 200

@app.route('/reports', methods=['GET'])
def search_reports():
    criteria = request.args.to_dict()
    results = report_controller.search(**criteria)
    return jsonify(results), 200


# D'autres routes CRUD pour les autres contrôleurs (Role, User, etc.)
# Exemples de routes supplémentaires :
# - @app.route('/users', methods=['POST'])
# - @app.route('/budgets/<budget_id>', methods=['PUT'])

if __name__ == '__main__':
    app.run(debug=False)
