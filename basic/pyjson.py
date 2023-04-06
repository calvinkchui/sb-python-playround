import json

# Functions
def demo():
  print("# pyjson.py")

  # String-2-json  
  x = '{ "name":"John", "age":30, "city":"New York"}'
  # parse x:
  y = json.loads(x)
  # the result is a Python dictionary:
  print(y["age"])

  # object-jsonString
  y = {"name": "John", "age": 30, "city": "New York"}
  # convert into JSON:
  x = json.dumps(y)
  # the result is a JSON string:
  print(x)
