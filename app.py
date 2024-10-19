from flask import Flask, jsonify, request
from Mongodb_class.Mongo_connect import MongoDBConnection
from classes.Controller.Controllers import (
    RoleController, UserController, AuditLogController, BudgetController,
    CategoryController, PeriodController, NotificationController, ExpenseController,
    ReportController, KPIController, ProjectController, RevenueController
)


app = Flask(__name__)
uri = "mongodb+srv://greylanisteur123:CWihvdE3IHnEV3eK@cluster0.i4xu4.mongodb.net/"
db_name = "Cluster1"
db_connection = MongoDBConnection(uri, db_name)


controllers = {
    "revenue": RevenueController(db_connection),
    "report": ReportController(db_connection),
    "role": RoleController(db_connection),
    "user": UserController(db_connection),
    "audit": AuditLogController(db_connection),
    "budget": BudgetController(db_connection),
    "category": CategoryController(db_connection),
    "period": PeriodController(db_connection),
    "notif": NotificationController(db_connection),
    "expense": ExpenseController(db_connection),
    "kpi": KPIController(db_connection),
    "project": ProjectController(db_connection),
}


def add_item(controller_name):
    data = request.json
    controllers[controller_name].add(data)
    return jsonify({"message": f"{controller_name.capitalize()} ajouté avec succès"}), 201

def delete_item(controller_name, item_id):
    controllers[controller_name].delete(item_id)
    return jsonify({"message": f"{controller_name.capitalize()} avec ID {item_id} supprimé."}), 200

def update_item(controller_name, item_id):
    data = request.json
    controllers[controller_name].update(item_id, data)
    return jsonify({"message": f"{controller_name.capitalize()} avec ID {item_id} mis à jour."}), 200

def search_items(controller_name):
    criteria = request.args.to_dict()
    results = controllers[controller_name].search(**criteria)
    return jsonify(results), 200

def get_all_items(controller_name) :
    results = controllers[controller_name].get_all()
    return jsonify(results), 200


@app.route('/<controller_name>', methods=['POST'])
def add(controller_name):
    return add_item(controller_name)

@app.route('/<controller_name>/<item_id>', methods=['DELETE'])
def delete(controller_name, item_id):
    return delete_item(controller_name, item_id)

@app.route('/<controller_name>/<item_id>', methods=['PUT'])
def update(controller_name, item_id):
    return update_item(controller_name, item_id)

@app.route('/<controller_name>', methods=['GET'])
def get_all(controller_name):
    return get_all_items(controller_name)

@app.route('/<controller_name>/search', methods=['GET'])
def search(controller_name):
    return search_items(controller_name)

# Exécution de l'application
if __name__ == '__main__':
    app.run(debug=False)
