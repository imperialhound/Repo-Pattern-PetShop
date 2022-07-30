from pydantic import BaseModel
from typing import Optional


# This is the expected request model
class Order(BaseModel):

    id: Optional[str]
    product: str
    quantity: int
