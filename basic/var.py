from collections import namedtuple


def demo():

  print("# variable")

  # Variable
  x = 1
  y = 3
  z = "Something"
  print(x, y, z)

  # local variables
  def myfunc():
    x = "fantastic"
    print("Python is " + x)

  myfunc()

  # DataType - https://www.w3schools.com/python/python_datatypes.asp

  x = "Hello World"  #str
  x = 20  #int
  x = 20.5  #float
  x = 1j  #complex
  x = ["apple", "banana", "cherry"]  #list
  x = ("apple", "banana", "cherry")  #tuple
  x = range(6)  #range
  x = {"name": "John", "age": 36}  #dict
  x = {"apple", "banana", "cherry"}  #set
  x = frozenset({"apple", "banana", "cherry"})  #frozenset
  x = True  # bool
  x = b"Hello"  #bytes
  x = bytearray(5)  #bytearray
  x = memoryview(bytes(5))  #memoryview
  x = None

  # Multiline String '''  or """"
  multilinestr = """Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
  sed do eiusmod tempor incididunt
  ut labore et dolore magna aliqua."""
  print(multilinestr)

  print('len', len(multilinestr))


def moreDemo():

  # Enumeration (enumerate)
  names = ["Alice", "Bob", "Charlie"]
  for index, name in enumerate(names):
    print(f"{index}: {name}")

  # Named tuple - immutable, you can’t modify them after creation
  Person = namedtuple('Person', ['name', 'age'])
  alice = Person(name="Alice", age=30)
  print(alice)

  # Dictionaries — get()
  # get() - When you want to retrieve a key’s value but aren’t sure it exists.
  # `setdefault()` - hen you want to set a default value if the key doesn’t exist.
  data = {"name": "Alice"}
  age = data.get("age", 30)
  data.setdefault("country", "USA")
  print(data)
