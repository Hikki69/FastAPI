from pydantic import BaseModel

class ProductDto(BaseModel):
    id:int
    title:str
    price:int=0
    count:int=0