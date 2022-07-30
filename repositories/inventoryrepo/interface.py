from abc import ABC, abstractmethod

class AbstractInventoryRepository(ABC):

    @abstractmethod
    def get_inventory(self):
        pass

    @abstractmethod
    def remove_inventory(self):
        pass
    