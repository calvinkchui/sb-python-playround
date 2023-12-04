def demo():
  #`zip()` allows combining multiple iterables, making it easier to loop through multiple lists in parallel.
  names = ["Alice", "Bob"]
  scores = [85, 92]
  for name, score in zip(names, scores):
    print(f"{name}: {score}")
  '''
  output:
  Alice: 85
  Bob: 92
  '''
