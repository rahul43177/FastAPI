from sys import api_version
from fastapi import APIRouter 
from fastapi_utils.cbv import cbv 
from pydantic import BaseModel
router = APIRouter(
    prefix="/inventory" ,
    tags=["Inventory"]
)


@cbv(router)
class InventoryManagementController : 
    def __init__(self):
        self.stock_left = 200 #Default Stock Left 
        self.po = "Purchase Order"
        self.system_version = "InventorySmart V.01"
        self.stock_naming = "New STOCK"
        self.tenant = "NA"


    @router.get("/stock")
    async def get_stock(self):
        return {
            "stock_left" : self.stock_left ,
            "po" : self.po ,
            "system_version" : self.system_version ,
            "stock_naming" : self.stock_naming ,
            "tenant" : self.tenant
        }
    @router.post("/stock/{stock_id}") 
    async def update_stock(self , stock_id : int , stock ):
        return  {
            "message" : f"Hello world {stock}"
        }

        
