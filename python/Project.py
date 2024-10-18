class Project:
    def __init__(self, project_id, project_name, start_date, end_date, created_by):
        self.project_id = project_id
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.created_by = created_by  # Association avec la classe User
