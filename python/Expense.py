class Expense:
    def __init__(self, expense_id, description, amount, date, category, project, created_by):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date
        self.category = category  # Association avec la classe Category
        self.project = project  # Association avec la classe Project
        self.created_by = created_by  # Association avec la classe User
