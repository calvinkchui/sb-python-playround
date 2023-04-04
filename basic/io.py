# Functions
def demo():
  print("# IO.py")

  # Open a file for WRITE
  fo = open("assets/foo.txt", "w")
  fo.write("Python is a great language.\nYeah its great!!\n")
  # Close opend file
  fo.close()

  # Open a file for READ
  fo = open("assets/foo.txt", "r+")
  str = fo.read(10)
  print("Read String is : ", str)
  # Close opend file
  fo.close()
