from fastapi import APIRouter

router = APIRouter()

@router.get("/userinfo/")
def get_user_info():
    return {"User info" : "List of users"}

@router.get("/userinfo/{user_id}/")
async def get_user_info_by_id(user_id : int):
    return {"user_id" : user_id}
