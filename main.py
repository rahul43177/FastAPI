from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root() :
    return {"message" : "gandu!"}


#normal method to extract from the body
@app.post("/greetings")
async def greetings(payload : dict = Body(...)):
    print("The payload is ->" , payload)
    name = payload.get("name")
    age = payload.get("age")
    gender = payload.get("gender")
    message = f"The name is -> {name} and the age is {age} and the gender is {gender}"
    information =  { 
        "greetings" : message , 
        "additional information" : {
            "name" : name , 
            "age" : age , 
            "gender" : gender
        }
    }
    return information 


#we created a Model
class Greet(BaseModel) :
    name : str 
    age : int 
    gender : str 

#using pydantic model for body -> we will only take that data
@app.post("/greet_user")
def greet_user(payload : Greet):
    print("payload" , payload)
    print("the type of payload->" ,type(payload))
    #now it will check the payload from the Greet model/class and if something extra or something is missing it will throw the error    
    user_info = {
        "name" : payload.name , 
        "age"  : payload.age  ,
        "gender" : payload.gender
    }
    return user_info