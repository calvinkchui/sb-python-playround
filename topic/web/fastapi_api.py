from fastapi import FastAPI

#app = FastAPI()
app = FastAPI(root_path="/proxy/8000/") 

'''
https://fastapi.tiangolo.com/tutorial/first-steps/

> python3 -m uvicorn fastapi_api:app --reload
'''

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


'''
Behind the Proxy
* https://fastapi.tiangolo.com/advanced/behind-a-proxy/

app = FastAPI(root_path="/proxy/8000/") 
'''
