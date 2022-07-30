from abc import ABC, abstractmethod
from domain.models.order import Order

class AbstractOrderRepository(ABC):

    @abstractmethod
    def add_order(self, order: Order) -> str:
        pass

    @abstractmethod
    def remove_order(self, order: Order) -> str:
        pass
    