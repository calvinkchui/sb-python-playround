'''
https://www.freecodecamp.org/news/python-one-liners/
'''
def demo01():
	# Using list comprehension
	squared_numbers = [i ** 2 for i in range(10)]
	print("squared_numbers:" , squared_numbers) # squared_numbers: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

	# Using Lambda
	add = lambda x, y: x + y
	print("lambda", add(2, 3)) # lambda 5

	# Map and Filter
	upper_case = list(map(lambda x: x.upper(), ['apple', 'banana', 'cherry']))
	print ("map-filter", upper_case) # map-filter ['APPLE', 'BANANA', 'CHERRY']

	# Ternary Operator
	num = 7
	result = "Even" if num % 2 == 0 else "Odd"
	print ("Ternary", result) # Ternary Odd

'''
10 Useful Python One-Liners for Data Cleaning
https://www.kdnuggets.com/10-useful-python-one-liners-for-data-cleaning
'''
def demo02():
	data = [
	{"name": "alice smith", "age": 30, "email": "alice@example.com", "salary": 50000.00, "join_date": "2022-03-15"},
	{"name": "bob gray", "age": 17, "email": "bob@not-an-email", "salary": 60000.00, "join_date": "invalid-date"},
	{"name": "charlie brown", "age": None, "email": "charlie@example.com", "salary": -1500.00, "join_date": "15-09-2022"},
	{"name": "dave davis", "age": 45, "email": "dave@example.com", "salary": 70000.00, "join_date": "2021-07-01"},
	{"name": "eve green", "age": 25, "email": "eve@example.com", "salary": None, "join_date": "2023-12-31"},
	]


    # Capitalizing the names for consistency
	data = [ {**d, "name": d["name"].title()} for d in data]    
	print( [ d["name"] for d in data ] ) # ['Alice Smith', 'Bob Gray', 'Charlie Brown', 'Dave Davis', 'Eve Green']

	# Converting age to an integer type, defaulting to 25 if conversion fails
	data = [{**d, "age": int(d["age"]) if isinstance(d["age"], (int, float)) else 25} for d in data]
	print( [ d["age"] for d in data ] ) # [30, 17, 25, 45, 25]

	# Ensuring age is an integer within the range of 18 to 60; otherwise, set to 25
	data = [{**d, "age": d["age"] if isinstance(d["age"], int) and 18 <= d["age"] <= 60 else 25} for d in data]
	print( [ d["age"] for d in data ] ) # [30, 25, 25, 45, 25]

	# Verifying that the email contains both an "@" and a "."; 
	#assigning 'invalid@example.com' if the format is incorrect
	data = [{**d, "email": d["email"] if "@" in d["email"] and "." in d["email"] else "invalid@example.com"} for d in data]
	print( [ d["email"] for d in data ] ) # ['alice@example.com', 'invalid@example.com', 'charlie@example.com', 'dave@example.com', 'eve@example.com']

	# Keeping only unique entries based on the name field
	data = {tuple(d.items()) for d in data}  # Using a set to remove duplicates
	#print( "tuple\n", data )
	data = [dict(t) for t in data]  # Converting back to list of dictionaries
	#print( "dict\n", data )

def demo():
	demo01()
	demo02()

