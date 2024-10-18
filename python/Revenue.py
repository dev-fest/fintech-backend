class Revenue:
    def __init__(self, revenue_id, description, amount, date, period, created_by):
        self.revenue_id = revenue_id
        self.description = description
        self.amount = amount
        self.date = date
        self.period = period  # Association avec la classe Period
        self.created_by = created_by  # Association avec la classe User

