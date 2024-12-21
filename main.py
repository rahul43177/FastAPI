from fastapi import FastAPI 
from fastapi.params import Body



app = FastAPI()

@app.get("/landingpage")
def read_root():
    return {"Hello": "World"}

@app.post("/hello_user")
def user_greeting():
    return {"message_for_user" : "Hello user how are you!"}

@app.post("/create_post")
async def create_post(payload : dict = Body(...)):
    print("Payload" , payload)
    return {"message" : "Rahul Mishra"}


@app.post("/create_post_with_body") 
async def create_post_with_body(payload : dict = Body(...)):
    print("payload ----" , payload)
    print("type of payload" , type(payload))
    title = payload['title']
    content = payload.get("content")

    print("Title " , title)
    print("content" , content)
    return {"message" : "Post created successfully"}



@app.post("/greet_user")
async def greet_user(payload : dict = Body(...)):
    print(f"Payload -> {payload}")
    name = payload.get("name")
    age = payload.get("age")
    gender = payload["gender"]
    print("The name , age and gender" , name , age , gender)
    message = f"Hello {name} you are {age} years old and your gender is {gender}" 
    return {"greeting" : message}