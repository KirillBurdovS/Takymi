from pydantic import BaseModel
from typing import List, Optional

class ExampleBase(BaseModel):
    name: str
    description: Optional[str] = None

class ExampleCreate(ExampleBase):
    pass

class ExampleUpdate(ExampleBase):
    pass

class Example(ExampleBase):
    id: int

    class Config:
        orm_mode = True

class ExampleList(BaseModel):
    examples: List[Example]