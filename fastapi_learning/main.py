from fastapi import FastAPI , Body
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

@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS_DATABASE)):
        if BOOKS_DATABASE[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS_DATABASE[i] = updated_book
            
@app.get("/books/allbook")
async def get_all_book():
    return BOOKS_DATABASE