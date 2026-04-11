from pydantic import BaseModel 
#pydantic is a data validation library that allows us to define data models with type annotations. It provides a way to validate and serialize data, making it easier to work with complex data structures.

class Todo(BaseModel):
    title: str
    description: str
    complete: bool