from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    name: str
    complete: bool