
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: str | None = Field(default=None)
    category: str | None = Field(default=None)
    image: str | None = Field(default=None)

# Modelo para crear una nuevo producto (hereda de ProductBase)
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass
