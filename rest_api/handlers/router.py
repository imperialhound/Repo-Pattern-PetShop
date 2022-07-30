
from fastapi import APIRouter
from rest_api.handlers import orderhandler

router = APIRouter()

router.include_router(orderhandler.router, tags=["order"])