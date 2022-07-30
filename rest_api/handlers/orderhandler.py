from fastapi import APIRouter
from rest_api.schema.status import Status
from rest_api.schema.order import Order
from domain.services.orderservice import OrderService
from domain.services.inventoryservice import InventoryService

from repositories.inventoryrepo.apiadapter import ApiAdapter
from repositories.orderrepo.sqladapter import SqlAdapter

from uuid import uuid4

# Set up Router
router = APIRouter()

# Initalize Order and inventory service. NOTE this is normally handled using dependency injection, so you can rotate between adapters 
# However, the purpose here is to just outline how the flow of dependencies should be managed from the domain layer to the repository layer

# Order service with SQL adapter
order_service = OrderService(order_repo=SqlAdapter()) # order_repo can be replaced with any adapter of the Order Repo interface

# Inventory service with API adapter
inventory_service = InventoryService(inventory_repo=ApiAdapter()) # inventory_repo can be replaced with any adapter of the Inventory Repo Interface 


@router.post("/add_order", response_model=Status, tags=["order"])
async def add_order(order: Order):

    # add unique uuid to new order
    order.id = uuid4()

    # Check product is in stock 
    status = inventory_service.check_stock(order)

    # If in stock add order else return Out of stock error
    if status.in_stock is True:
        message = order_service.add_order(order)
        inventory_service.adjust_stock(order)
        status.message = message
    
    else:
        status.message = "Out of Stock"
    
    return status

@router.post("/remove_order", response_model=Status, tags=["order"])
async def remove_order(order: Order):

    message = order_service.remove_order(order)
    return Status(message=message)