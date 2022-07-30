import uvicorn
import logging
from fastapi import FastAPI
from rest_api.handlers.router import router as api_router

# Initalize logger
logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
logging.getLogger("API").setLevel(logging.INFO)


# Starts PetShop Order API
def get_service() -> FastAPI:

    application = FastAPI(title="PetShop Order API")
    application.include_router(api_router)

    return application
