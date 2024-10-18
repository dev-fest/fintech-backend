from pydantic import BaseModel, Field
from datetime import datetime
from classes.User import User

class AuditLog(BaseModel):
    log_id: int = Field(..., ge=1, description="L'ID du log doit être un entier positif.")
    user: User  # Association avec la classe User
    action: str = Field(..., min_length=3, max_length=100, description="L'action doit être décrite entre 3 et 100 caractères.")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Getter et Setter pour log_id
    @property
    def get_log_id(self) -> int:
        return self.log_id

    @get_log_id.setter
    def set_log_id(self, value: int):
        if value < 1:
            raise ValueError("log_id doit être un entier positif.")
        self.log_id = value

    # Getter et Setter pour action
    @property
    def get_action(self) -> str:
        return self.action

    @get_action.setter
    def set_action(self, value: str):
        if not (3 <= len(value) <= 100):
            raise ValueError("L'action doit contenir entre 3 et 100 caractères.")
        self.action = value

    # Getter et Setter pour timestamp
    @property
    def get_timestamp(self) -> datetime:
        return self.timestamp

    @get_timestamp.setter
    def set_timestamp(self, value: datetime):
        if value > datetime.utcnow():
            raise ValueError("Le timestamp ne peut pas être dans le futur.")
        self.timestamp = value

