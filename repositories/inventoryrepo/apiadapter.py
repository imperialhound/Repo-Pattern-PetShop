from repositories.inventoryrepo.interface import AbstractInventoryRepository
from domain.models.inventory import Inventory
from domain.models.order import Order

# NOTE: Missing actual logic just for representation

class ApiAdapter(AbstractInventoryRepository):

    def get_inventory(self, order: Order) -> Inventory:
        return Inventory(order.product, 100)
    
    def remove_inventory(self, order: Order) -> str:
        return f"Successful removed {order.quantity}"
