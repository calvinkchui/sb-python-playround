
# list comprehensions
x = [1, 2, 3, 4, 5]
y = [2*a for a in x if a % 2 == 1]
print(y) # [2, 6, 10]


# Append (+)
a1 = [1,2,3,4,5]
a2 = [6,7,8,9]
a1 + a2 # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Copy to a new array[]
array2 = array[:]