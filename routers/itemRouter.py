from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
async def get_item_details():
    item_dict = {
        "item-1" : {
            "name" : "Mac Book" , 
            "color" : "Chrome" , 
            "spec" : "intel"
        } , 
        "item-2" : {
            "name" : "iPhone" , 
            "color" : "Blue" , 
            "spec" : "some chip"
        }
    }
    
    return item_dict
    