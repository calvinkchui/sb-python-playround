from fastapi import FastAPI

'from .moduleName import xxx' 
import fastapi_routers


#app = FastAPI()
app = FastAPI(root_path="/proxy/8000/",

# document
    title="Sandbox FastAPI",
    description="Fast API - demo application",
    summary="test functions"

) 

'''
https://fastapi.tiangolo.com/tutorial/first-steps/

> cd topic/web/
> python3 -m uvicorn fastapi_api:app --reload
'''

'''
Behind the Proxy
* https://fastapi.tiangolo.com/advanced/behind-a-proxy/

app = FastAPI(root_path="/proxy/8000/") 
'''

# External Router
app.include_router(fastapi_routers.router)

# First Step
@app.get("/")
async def root():
    return {"message" : "Hello World!"}

'''
Generated openapi - http://xxx/openapi.json

{"openapi":"3.1.0","info":
  {"title":"FastAPI","version":"0.1.0"},
   "paths":{
      "/":{
          "get":{
            "summary":"Root",
            "operationId":"root__get",
            "responses":{
                "200":{
                    "description":"Successful Response",
                    "content":{"application/json":{"schema":{}
}}}}}}}}
'''




# Path Parameter
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}



# Query Parameter
# path: /items/?skip=0&limit=10
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



