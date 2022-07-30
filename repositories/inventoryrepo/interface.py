from abc import ABC, abstractmethod
from domain.models.inventory import Inventory
from domain.models.order import Order

class AbstractInventoryRepository(ABC):

    @abstractmethod
    def get_inventory(self, product: str) -> Inventory:
        pass

    @abstractmethod
    def remove_inventory(self, order: Order) -> str:
        pass
    