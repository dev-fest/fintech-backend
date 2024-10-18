from pydantic import BaseModel, Field, validator

class Role(BaseModel):
    role_id: int = Field(..., ge=1, description="L'ID du rôle doit être un entier positif.")
    role_name: str = Field(..., min_length=3, max_length=50, description="Le nom du rôle doit contenir entre 3 et 50 caractères.")

    # Getter pour role_id
    @property
    def get_role_id(self) -> int:
        return self.role_id

    # Setter pour role_id
    @get_role_id.setter
    def set_role_id(self, value: int):
        if value < 1:
            raise ValueError("role_id doit être un entier positif.")
        self.role_id = value

    # Getter pour role_name
    @property
    def get_role_name(self) -> str:
        return self.role_name

    # Setter pour role_name
    @get_role_name.setter
    def set_role_name(self, value: str):
        if not (3 <= len(value) <= 50):
            raise ValueError("role_name doit contenir entre 3 et 50 caractères.")
        self.role_name = value

    # Validation personnalisée (facultatif)
    @validator('role_name')
    def validate_role_name(cls, v):
        if not v.isalpha():
            raise ValueError("Le nom du rôle doit contenir uniquement des lettres.")
        return v
