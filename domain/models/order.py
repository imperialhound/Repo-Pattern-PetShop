from dataclasses import dataclass

# This model represents the data of a individual order

@dataclass(frozen=True)
class Order:
    id: str # The id of a unique order 
    product: str # The name of the product
    quantity: int # The quantity desired
