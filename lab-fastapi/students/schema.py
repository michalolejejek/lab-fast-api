from pydantic import BaseModel

class StudentUpdateSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None