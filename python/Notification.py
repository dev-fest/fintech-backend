class Notification:
    def __init__(self, notification_id, user, message, status, created_at):
        self.notification_id = notification_id
        self.user = user  # Association avec la classe User
        self.message = message
        self.status = status  # 'unread' ou 'read'
        self.created_at = created_at
