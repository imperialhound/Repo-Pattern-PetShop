from repositories.orderrepo.interface import AbstractOrderRepository
from domain.models.inventory import Inventory
from domain.models.order import Order

# NOTE: Missing actual logic just for representation

class ApiAdapter(AbstractOrderRepository):

    def add_order(self, order: Order) -> str:
        return f"Order added successfully"
    
    def remove_order(self, order: Order) -> str:
        return f"Order Removed successfully"