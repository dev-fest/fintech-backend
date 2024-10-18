from pydantic import BaseModel, Field
from datetime import datetime
from period import Period
from user import User

class Report(BaseModel):
    report_id: int = Field(..., ge=1, description="L'ID du rapport doit être un entier positif.")
    report_type: str = Field(..., min_length=1, description="Le type de rapport ne peut pas être vide.")
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    period: Period
    created_by: User

    @property
    def get_report_type(self) -> str:
        return self.report_type

    @get_report_type.setter
    def set_report_type(self, value: str):
        if not value.strip():
            raise ValueError("Le type de rapport ne peut pas être vide.")
        self.report_type = value
