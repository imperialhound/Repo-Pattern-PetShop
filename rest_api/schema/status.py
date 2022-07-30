from pydantic import BaseModel
from typing import Optional

# This is the expected response model
class Status(BaseModel):
    in_stock: Optional[bool]
    message: str
