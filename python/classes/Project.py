from pydantic import BaseModel, Field, validator
from datetime import date
from User import User

class Project(BaseModel):
    project_id: int = Field(..., ge=1, description="L'ID du projet doit être un entier positif.")
    project_name: str = Field(..., min_length=1, description="Le nom du projet ne peut pas être vide.")
    start_date: date
    end_date: date
    created_by: User

    @validator('end_date')
    def validate_dates(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError("La date de fin doit être postérieure à la date de début.")
        return v

    @property
    def get_project_name(self) -> str:
        return self.project_name

    @get_project_name.setter
    def set_project_name(self, value: str):
        if not value.strip():
            raise ValueError("Le nom du projet ne peut pas être vide.")
        self.project_name = value
