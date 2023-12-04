from functools import reduce


# map():  every item of a collection.
# filter():  select items based on a predicate.
# reduce(): cumulatively apply a function to items,
#
# Note: map() & filter() return `iterators`, it should covert by `list()`
def demo():

  # `map()`
  names = ["alice", "bob", "charlie"]
  upper_names = list(map(str.upper, names))

  print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

  # `reduce()`
  cart = [{"name": "item1", "price": 50}, {"name": "item2", "price": 100}]
  total = reduce(lambda x, y: x + y['price'], cart, 0)
  print(total)  #150
