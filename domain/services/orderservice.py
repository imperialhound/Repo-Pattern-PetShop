from domain.models.order import Order
from repositories.orderrepo.interface import AbstractOrderRepository

# AS you can see the service recieves the repository without knowledge of what the original data source is. 


class OrderService:

    def __init__(self, order_repo: AbstractOrderRepository):
        self.order_repo = order_repo

    def add_order(self, order: Order) -> str:
        message = self.order_repo.add_order(order)
        return message

    def remove_order(self, order: Order) -> str:
        message = self.order_repo.remove_order(order)
        return message

        
