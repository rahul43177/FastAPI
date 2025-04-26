# Path Parameters

Path parameters are variables that are part of the URL path in an API endpoint. They are used to capture specific values from the URL and pass them to the backend for processing.

## Syntax in FastAPI

In FastAPI, path parameters are defined by including curly braces `{}` in the path string. For example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

## Key Points
- Path parameters are mandatory and must match the specified format in the URL.
- They can be type-annotated to enforce data validation (e.g., `int`, `str`).
- FastAPI automatically parses and validates the path parameter based on the type annotation.

## Example

```python
@app.get("/users/{user_id}/posts/{post_id}")
async def read_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}
```

In this example:
- `user_id` and `post_id` are path parameters.
- The endpoint `/users/123/posts/456` would return:
  ```json
  {
      "user_id": 123,
      "post_id": 456
  }
  ```

## Notes
- Path parameters are case-sensitive.
- Avoid using special characters in parameter names.
- Use descriptive names for better readability.
