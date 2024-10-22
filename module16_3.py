from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def user_get() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def user_post(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def user_put(user_id: Annotated[str, Path()],
                   username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path()]) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'
