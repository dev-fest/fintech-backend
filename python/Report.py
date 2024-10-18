class Report:
    def __init__(self, report_id, report_type, generated_at, period, created_by):
        self.report_id = report_id
        self.report_type = report_type
        self.generated_at = generated_at
        self.period = period  # Association avec la classe Period
        self.created_by = created_by  # Association avec la classe User
