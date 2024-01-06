import pandas as pd

# Series - Column
# see - https://www.w3schools.com/python/pandas/pandas_series.asp
a = [1, 7, 2]
myvar = pd.Series(a)
print('# Series')
print(myvar)
myvar = pd.Series(a, index = ["x", "y", "z"])
print('# Series with label')
print(myvar)

'''
# Series
0    1
1    7
2    2
dtype: int64
# Series with label
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
print(myvar)

'''
# DataFame
   calories  duration
0       420        50
1       380        40
2       390        45
'''