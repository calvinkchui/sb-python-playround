import pandas as pd

# DataFrames - Table
data = {
  "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "odd": [1, 3, 5, 7 ,9, 11, 13, 15, 17, 19],
  "even": [2, 4, 6, 8 ,10, 12, 14, 16, 18, 20],
}
index_labels=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10']
df = pd.DataFrame(data, index=index_labels)

# How to Get Cell Value From DataFrame?
# loc[row name][column name]
# iloc[row index][column index]
# at[row name, column name]
# iat[row index, column index]

# Using loc[]. Get cell value by Column name 
print("Column name ['r4']['list']:" , df.loc['r4']['list'])
#print(df.loc['r4'][2]) #deprecated

# Using iloc[]. Get cell value by Column Position
print("Column Position [4]['list']:", df.iloc[4]['list'])
#print("Column Position [4][2]:", df.iloc[4][2]) # depercated

'''
name & index ['r4']['list']: 4
Column Position [4]['list']: 5
'''
# Using at[]. Select Specific Cell Value by Column Label Name
print("Column Label Name ['r4','list']:", df.at['r4','list'])
# Using iat[]. Select Specific Cell Value by Column Position
print("Column Position [3,2]:", df.iat[3,2])
'''
Column Label Name ['r4','list']: 4
Column Position [3,2]: 8
'''

# Select Cell Value from DataFrame Using df[‘col_name’].values[]
print("df[‘col_name’].values[]:", df["list"].values[3])

'''
df[‘col_name’].values[]: 4
'''
