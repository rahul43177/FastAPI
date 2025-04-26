from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    { "title": "Title One", "author": "Author One", "category": "science" },
    { "title": "Title Two", "author": "Author Two", "category": "science" },
    { "title": "Title Three", "author": "Author Three", "category": "history" },
    { "title": "Title Four", "author": "Author Four", "category": "math" },
    { "title": "Title Five", "author": "Author Five", "category": "math" },
    { "title": "Title Six", "author": "Author Two", "category": "math" }
]

@app.get("/books")
async def read_all_books():
    return BOOKS

# PATH PARAMETERS 
@app.get("/books/{book_id}")
async def get_book_by_id(book_id : int) :
    length = len(BOOKS)
    print(f"The book id : {book_id}")
    if book_id > length : 
        return {"message" : "ID Does not exist"}
    return BOOKS[book_id]