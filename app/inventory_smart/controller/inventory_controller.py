from fastapi import APIRouter
from fastapi_utils.cbv import  cbv
router = APIRouter(
    prefix="/inventory" ,
    tags=["Inventory"]
)
@cbv(router)
class InventoryController :
    def __init__(self):
        self.system_version = "InventorySmart V.01"
        self.stock_naming = "New STOCK"

    @router.get("/stock")
    async def get_stock(self):
        return {
            "version" : self.system_version ,
            "stock" : self.stock_naming
        }



