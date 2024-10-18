from pydantic import BaseModel, Field, validator
from datetime import date
from period import Period
from user import User

class Revenue(BaseModel):
    revenue_id: int = Field(..., ge=1, description="L'ID du revenu doit être un entier positif.")
    description: str = Field(..., min_length=1, description="La description ne peut pas être vide.")
    amount: float = Field(..., gt=0, description="Le montant doit être positif.")
    date: date
    period: Period
    created_by: User

    @property
    def get_description(self) -> str:
        return self.description

    @get_description.setter
    def set_description(self, value: str):
        if not value.strip():
            raise ValueError("La description ne peut pas être vide.")
        self.description = value

    @property
    def get_amount(self) -> float:
        return self.amount

    @get_amount.setter
    def set_amount(self, value: float):
        if value <= 0:
            raise ValueError("Le montant doit être positif.")
        self.amount = value
