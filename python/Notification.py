from pydantic import BaseModel, Field, validator
from datetime import datetime
from User import User  # Association avec User

class Notification(BaseModel):
    notification_id: int = Field(..., ge=1, description="L'ID de la notification doit être un entier positif.")
    user: User  # Association avec la classe User
    message: str = Field(..., min_length=1, description="Le message ne peut pas être vide.")
    status: str = Field(..., regex='^(unread|read)$', description="Le statut doit être 'unread' ou 'read'.")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Validation personnalisée pour le statut
    @validator('status')
    def validate_status(cls, v):
        if v not in ['unread', 'read']:
            raise ValueError("Le statut doit être 'unread' ou 'read'.")
        return v

    # Getter et Setter pour message
    @property
    def get_message(self) -> str:
        return self.message

    @get_message.setter
    def set_message(self, value: str):
        if not value.strip():
            raise ValueError("Le message ne peut pas être vide.")
        self.message = value

    # Getter et Setter pour status
    @property
    def get_status(self) -> str:
        return self.status

    @get_status.setter
    def set_status(self, value: str):
        if value not in ['unread', 'read']:
            raise ValueError("Le statut doit être 'unread' ou 'read'.")
        self.status = value
