from pydantic import BaseModel
from typing import List, Optional

class ExampleBase(BaseModel):
    name: str
    description: Optional[str] = None

class ExampleCreate(BaseModel):
    name: str
    description: str

class ExampleUpdate(BaseModel):
    name: str
    description: str

class ExampleResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True

class ExampleList(BaseModel):
    examples: List[ExampleResponse]