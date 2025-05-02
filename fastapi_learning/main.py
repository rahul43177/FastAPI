from fastapi import FastAPI , Body
from pydantic import BaseModel, field_validator

app  = FastAPI()

BOOKS = [
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
        
class AddBookClass(BaseModel):
    id : int 
    title : str 
    author : str 
    year : int 
    genre : str 

    @field_validator("year")
    def year_validation(cls, v):
        if not isinstance(v, int):
            raise ValueError("Year must be an integer, not a string")
        if v < 0:
            raise ValueError("Year must be greater than 0")
        return v
        
    
    
@app.post("/addbook")
async def add_book_database(single_book_data : AddBookClass):
    print("Body" , single_book_data)
    print(f"The type of book is : {type(single_book_data)}")
    BOOKS.append(single_book_data)
    return {
        "message" : "The book data added successfully" ,  
        "updated book data" : BOOKS
    } 

class BookId(BaseModel):
    id : int

    @field_validator("id")
    def id_validator(cls , v):
        if v < 0 :
            raise ValueError("Id can't be negative")
        return v 


# @app.post("/fetchbook")
# async def fetch_book_by_id(book_id: BookId):
#     book_to_return = []
#     for book in BOOKS:
#         if book.get("id") == book_id.id:
#             book_to_return.append(book)
#     if not book_to_return:
#         return {
#             "message": "No book found with the given ID"
#         }
#     return {
#         "book": book_to_return
#     }

@app.post("/fetchbook")
async def fetch_book_by_id(book_id : BookId):
    book_to_return = []
    for book in BOOKS:
        if book.get("id") == book_id.id:
            book_to_return.append(book)
    if not book_to_return:
        return {
            "message" : "No book fount with the given ID"
        }
    return {
        "book" : book_to_return
    }


