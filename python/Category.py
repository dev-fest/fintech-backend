from pydantic import BaseModel, Field

class Category(BaseModel):
    category_id: int = Field(..., ge=1, description="L'ID de la catégorie doit être un entier positif.")
    category_name: str = Field(..., min_length=1, description="Le nom de la catégorie ne peut pas être vide.")

    # Getter et Setter pour category_name
    @property
    def get_category_name(self) -> str:
        return self.category_name

    @get_category_name.setter
    def set_category_name(self, value: str):
        if not value.strip():
            raise ValueError("Le nom de la catégorie ne peut pas être vide.")
        self.category_name = value

