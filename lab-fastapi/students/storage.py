from functools import lru_cache
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

students_db = {
    1: {"first_name": "John", "last_name": "Doe"},
    2: {"first_name": "Jane", "last_name": "Smith"},
}

@lru_cache
def get_students():
    return students_db