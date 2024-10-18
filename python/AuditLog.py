class AuditLog:
    def __init__(self, log_id, user, action, timestamp):
        self.log_id = log_id
        self.user = user  # Association avec la classe User
        self.action = action
        self.timestamp = timestamp