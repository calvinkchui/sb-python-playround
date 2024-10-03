import pandas as pd

# Dropping - Series
s = pd.Series( [1, 7, 2], index = ["x", "y", "z"])
s2 = s.drop(['x']) # drop value from rows (axis=0)
print(s2)

'''
y    7
z    2
dtype: int64
'''

# Dropping - Dataframe
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
df2 = df.drop("calories", axis=1) # drop value from column(axis=1)
print(df2)

'''
   duration
0        50
1        40
2        45
'''