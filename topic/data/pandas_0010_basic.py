import pandas as pd

# Series - Column
# see - https://www.w3schools.com/python/pandas/pandas_series.asp
a = [1, 7, 2]
myvar = pd.Series(a)
print('# Series')
print(myvar)

'''
# Series
0    1
1    7
2    2
'''

print('# Series - Add index')
myvar.index = ["x", "y", "z"]
print(myvar)

myvar = pd.Series(a, index = ["x", "y", "z"])
print('# Series - create with index')
print(myvar)

'''
dtype: int64
# Series - Add index
x    1
y    7
z    2
dtype: int64
# Series - create with index
x    1
y    7
z    2
dtype: int64
'''



# Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print('# Series - Key/Value')
print(myvar)

'''
# Series - Key/Value
day1    420
day2    380
day3    390
dtype: int64
'''



# DataFrames - Table
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print('# DataFame')
print(myvar.tail())
print(myvar.describe())
'''
# DataFame
   calories  duration
0       420        50
1       380        40
2       390        45

         calories  duration
count    3.000000       3.0
mean   396.666667      45.0
std     20.816660       5.0
min    380.000000      40.0
25%    385.000000      42.5
50%    390.000000      45.0
75%    405.000000      47.5
max    420.000000      50.0
'''

