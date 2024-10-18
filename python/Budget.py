class Budget:
    def __init__(self, budget_id, amount, start_date, end_date, category, project):
        self.budget_id = budget_id
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
        self.category = category  # Association avec la classe Category
        self.project = project  # Association avec la classe Project
