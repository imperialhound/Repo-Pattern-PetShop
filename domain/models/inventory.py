from dataclasses import dataclass

# This model represents the inventory of a given product

@dataclass
class Inventory:
    product: str # The name of the product
    quantity: int # The quantity desired