from fastapi import FastAPI,Request
from mockdata import product
from dtos import ProductDto

app = FastAPI()


@app.get("/")
def home ():
    return "hello nigga"


@app.get("/product")
def getProducts():
    return product

## path params
@app.get("/product/{product_id}")
def getOneProduct(product_id:int):

    for oneProduct in product:
        if oneProduct.get("id") == product_id:
            return oneProduct

    return {
        "error": "Product not found with this id."
    }

## query params
@app.get("/greet")
def greet(request:Request):
    queryParams = dict(request.query_params)
    print(queryParams)
    return {
        "greet":f"Yo {queryParams.get("name")}, wyd"
    }


## we can send data by 3 ways - body data(post/put), header-request headers, query params

## different types of HTTP Methods

@app.post("/create_product")
def createProduct(product_data:ProductDto):
    product_data = product_data.model_dump()
    product.append(product_data)
    return {"status":"Product created successfully..","data":product}


@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDto,product_id:int):
    for index,oneProduct in enumerate(product):
        if oneProduct.get("id") == product_id:
            product[index]= product_data.model_dump()
            return {"status":"Product Updated Successfully...","product":product_data}

    return {
        "error": "Product not found with this id."
    } 

## pydantic will recive the data from the client on the backend

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,oneProduct in enumerate(product):
        if oneProduct.get("id") == product_id:
            deleted_product = product.pop(index)
            return {"status":"Product Deleted Successfully...","product":deleted_product}
        
    return {
        "error":"Product Not Found For This ID"
    }