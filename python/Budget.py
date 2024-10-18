from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional
from category import Category  # Classe associée
from project import Project  # Classe associée

class Budget(BaseModel):
    budget_id: int = Field(..., ge=1, description="L'ID du budget doit être un entier positif.")
    amount: float = Field(..., gt=0, description="Le montant doit être un nombre positif.")
    start_date: date
    end_date: date
    category: Optional[Category]  # Association avec Category
    project: Optional[Project]  # Association avec Project

    # Validation personnalisée des dates
    @validator('end_date')
    def validate_dates(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError("La date de fin doit être postérieure à la date de début.")
        return v

    # Getter et Setter pour amount
    @property
    def get_amount(self) -> float:
        return self.amount

    @get_amount.setter
    def set_amount(self, value: float):
        if value <= 0:
            raise ValueError("Le montant doit être supérieur à zéro.")
        self.amount = value

    # Getter et Setter pour start_date
    @property
    def get_start_date(self) -> date:
        return self.start_date

    @get_start_date.setter
    def set_start_date(self, value: date):
        if value > self.end_date:
            raise ValueError("La date de début doit être antérieure à la date de fin.")
        self.start_date = value

    # Getter et Setter pour end_date
    @property
    def get_end_date(self) -> date:
        return self.end_date

    @get_end_date.setter
    def set_end_date(self, value: date):
        if value < self.start_date:
            raise ValueError("La date de fin doit être postérieure à la date de début.")
        self.end_date = value
