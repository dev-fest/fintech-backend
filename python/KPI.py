from pydantic import BaseModel, Field
from datetime import date

class KPI(BaseModel):
    kpi_id: int = Field(..., ge=1, description="L'ID du KPI doit être un entier positif.")
    name: str = Field(..., min_length=1, description="Le nom du KPI ne peut pas être vide.")
    value: float = Field(..., description="La valeur du KPI doit être un nombre.")
    date: date

    @property
    def get_name(self) -> str:
        return self.name

    @get_name.setter
    def set_name(self, value: str):
        if not value.strip():
            raise ValueError("Le nom du KPI ne peut pas être vide.")
        self.name = value

    @property
    def get_value(self) -> float:
        return self.value

    @get_value.setter
    def set_value(self, value: float):
        if value < 0:
            raise ValueError("La valeur du KPI ne peut pas être négative.")
        self.value = value
