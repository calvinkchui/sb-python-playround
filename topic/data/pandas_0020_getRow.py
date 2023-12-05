import pandas as pd

# DataFrames - Table
data = {
  "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "odd": [1, 3, 5, 7 ,9, 11, 13, 15, 17, 19],
  "even": [2, 4, 6, 8 ,10, 12, 14, 16, 18, 20],
}
#index_labels=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10']
df = pd.DataFrame(data)


# Select Rows by Index Position
#see - https://sparkbyexamples.com/pandas/pandas-select-rows-by-index/
# `.loc[ row index ]`

print('\n# Select Rows by Index Position')
df2 = df.iloc[2]     # Select Row by Index
print (df2)
'''
r1    3
r2    5
r3    6
'''

df2 = df.iloc[[2,3,6]]  # Select Rows by Index List
print (df2)
'''
   r1  r2  r3
2   3   5   6
3   4   7   8
6   7  13  14
'''
df2 = df.iloc[1:5]   # Select Rows by Integer Index Range
print (df2)
df2 = df.iloc[:1]    # Select First Row
print (df2)
df2 = df.iloc[:3]    # Select First 3 Rows
print (df2)
df2 = df.iloc[-1:]   # Select Last Row
print (df2)
df2 = df.iloc[-3:]   # Select Last 3 Row
print (df2)
df2 = df.iloc[::2]   # Selects alternate rows
print (df2)
'''
   r1  r2  r3
0   1   1   2
2   3   5   6
4   5   9  10
6   7  13  14
8   9  17  18
'''

# Select Rows by Index Labels
index_labels=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10']
df = pd.DataFrame(data,index=index_labels)

print('\n# Select Rows by Index Labels')
df2 = df.loc['r2']          # Select Row by Index Label
print ('r2:\n', df2)
'''
list    2
odd     3
even    4
Name: r2, dtype: int64
'''
#df2 = df.loc[['r2','r3','r6']]    # Select Rows by Index Label List
#df2 = df.loc['r1':'r5']     # Select Rows by Label Index Range
#df2 = df.loc['r1':'r5']     # Select Rows by Label Index Range
#df2 = df.loc['r1':'r5':2]   # Select Alternate Rows with in Index Labels
