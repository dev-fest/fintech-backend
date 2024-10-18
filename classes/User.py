from pydantic import BaseModel, Field, EmailStr, validator, ValidationError
from typing import Optional
import re
from classes.Role import Role


class User(BaseModel):
    user_id: int = Field(..., ge=1, description="L'ID de l'utilisateur doit être un entier positif.")
    first_name: str = Field(..., min_length=2, max_length=30, description="Le prénom doit contenir entre 2 et 30 caractères.")
    last_name: str = Field(..., min_length=2, max_length=30, description="Le nom doit contenir entre 2 et 30 caractères.")
    email: EmailStr = Field(..., description="L'email doit être valide.")
    password_hash: str = Field(..., min_length=8, description="Le mot de passe doit contenir au moins 8 caractères.")
    role: Optional[Role] = Field(..., description="Le rôle de l'utilisateur.")

    # Getter et Setter pour user_id
    @property
    def get_user_id(self) -> int:
        return self.user_id

    @get_user_id.setter
    def set_user_id(self, value: int):
        if value < 1:
            raise ValueError("user_id doit être un entier positif.")
        self.user_id = value

    # Getter et Setter pour first_name
    @property
    def get_first_name(self) -> str:
        return self.first_name

    @get_first_name.setter
    def set_first_name(self, value: str):
        if not (2 <= len(value) <= 30):
            raise ValueError("Le prénom doit contenir entre 2 et 30 caractères.")
        self.first_name = value

    # Getter et Setter pour last_name
    @property
    def get_last_name(self) -> str:
        return self.last_name

    @get_last_name.setter
    def set_last_name(self, value: str):
        if not (2 <= len(value) <= 30):
            raise ValueError("Le nom doit contenir entre 2 et 30 caractères.")
        self.last_name = value

    # Getter et Setter pour email
    @property
    def get_email(self) -> str:
        return self.email

    @get_email.setter
    def set_email(self, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("L'email n'est pas valide.")
        self.email = value

    # Getter et Setter pour password_hash
    @property
    def get_password_hash(self) -> str:
        return self.password_hash

    @get_password_hash.setter
    def set_password_hash(self, value: str):
        if len(value) < 8:
            raise ValueError("Le mot de passe doit contenir au moins 8 caractères.")
        self.password_hash = value

    # Validation supplémentaire pour le prénom et le nom
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if not v.isalpha():
            raise ValueError("Le prénom et le nom doivent contenir uniquement des lettres.")
        return v