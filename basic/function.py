# Functions
def demo():
  print("# function.py")

  def my_function():
    print("Hello from a function")

  my_function()

  #   Arbitrary Arguments, *args
  def my_function(*kids):
    print("The youngest child is " + kids[2])

  my_function("Emil", "Tobias", "Linus")

  #    Keyword Arguments ( key = value)
  def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

  my_function(child1="Emil", child2="Tobias", child3="Linus")

  #    Arbitrary Keyword Arguments, **kwargs
  def my_function(**kid):
    print("His last name is " + kid["lname"])

  my_function(fname="Tobias", lname="Refsnes")

  #    Default Parameter Value
  def my_function(country="Norway"):
    print("I am from " + country)

  my_function()

  # Lambda ```lambda arguments : expression```
  #   anonymous function i
  print("## lambda")
  x = lambda a: a + 10
  print(x(5))
