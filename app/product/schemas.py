
from sqlmodel import Field, SQLModel
from typing import Optional

class ProductBase(SQLModel):
    title: str
    price: int = 0
    description: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None

# Modelo para crear un nuevo producto
class ProductCreate(ProductBase):
    pass

# Modelo para actualizar un producto
class ProductUpdate(ProductBase):
    pass

# Modelo para leer un producto con ID
class ProductRead(ProductBase):
    id: int
