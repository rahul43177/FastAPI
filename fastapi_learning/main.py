from fastapi import FastAPI
from pydantic import BaseModel , field_validator
app = FastAPI()

BOOKS_DATABASE = [
    {
        "id": 1,
        "title": "Mathematics",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 2,
        "title": "Physics",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 3,
        "title": "Chemistry",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 4,
        "title": "Biology",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 5,
        "title": "Computer Science",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 6,
        "title": "History",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 7,
        "title": "Geography",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 8,
        "title": "Economics",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 9,
        "title": "Political Science",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 10,
        "title": "English",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    },
    {
        "id": 11,
        "title": "Science",
        "author": "NCERT",
        "year": 2022,
        "genre": "Academic"
    }
]


CARS_DATABASE = [
    {
        "id": 1,
        "make": "Toyota",
        "model": "Camry",
        "year": 2022,
        "color": "Silver",
        "price": 25000
    },
    {
        "id": 2,
        "make": "Honda",
        "model": "Civic",
        "year": 2023,
        "color": "Blue",
        "price": 22000
    },
    {
        "id": 3,
        "make": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "color": "White",
        "price": 45000
    },
    {
        "id": 4,
        "make": "Ford",
        "model": "Mustang",
        "year": 2022,
        "color": "Red",
        "price": 35000
    },
    {
        "id": 5,
        "make": "BMW",
        "model": "X5",
        "year": 2023,
        "color": "Black",
        "price": 65000
    }
]


@app.get("/getallbooks")
def get_all_books():
    return BOOKS_DATABASE

# add a new book to database 
class AddBook(BaseModel):
    id : int 
    title : str 
    author : str 
    year : int 
    genre : str

    @field_validator("id")
    def validate_id(cls , v) :
        if v < 0:
            return {"message" : "THe id can't be negative"}
        if isinstance(v , str):
            return {"mssage" : "The id can't be a string"}
        return v 
        

@app.post("/addbook")
def add_new_book(single_book : AddBook):
    BOOKS_DATABASE.append(single_book)
    return {
        "message" : "The data has been added" , 
        "book data" : BOOKS_DATABASE
    }
    

#i want a add car to database API
class AddCar(BaseModel):
    id : int 
    make : str 
    model : str 
    year : int 
    color : str 
    price : int 

@app.post("/addcar")
def add_new_car(single_car : AddCar):
    CARS_DATABASE.append(single_car)
    return {
        "message" : "The data has been added" , 
        "car data" : CARS_DATABASE
    }


#i want a get all cars from database API
@app.get("/getallcars")
def get_all_cars():
    return CARS_DATABASE


#i want a get a single car from database API
@app.get("/getcar/{car_id}")
def get_single_car(car_id : int):
    for car in CARS_DATABASE:
        if car["id"] == car_id:
            return car
    return {"message" : "The car is not found"} 
        