from domain.models.order import Order
from repositories.inventoryrepo.interface import AbstractInventoryRepository
from domain.models.status import Status


class InventoryService:

    def __init__(self, inventory_repo: AbstractInventoryRepository):
        self.inventory_repo = inventory_repo

    def check_stock(self, order: Order) -> Status:
        inventory = self.inventory_repo.get_inventory(order)

        if inventory.quantity != 0:
            return Status(True, None)
        
        else:
            return Status(False, None)

    def adjust_stock(self, order: Order) -> str:
        message = self.inventory_repo.remove_inventory(order)

        return message
        