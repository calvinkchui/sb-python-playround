import pandas as pd
from dataframe_diff import dataframe_diff


prior_data = {'Date': ['30-Nov','30-Nov','30-Nov','30-Nov', '30-Nov'],
          'ID': ['0001','0002','0003','0004', '0005'],
          'Value' : [100.00, 200.00, 300.00, 450.00, 500.00],
          'Category' : ['A','B','C','D','D'],
          'Subcategory' : ['A100','B120','C300','D900','D900']}


current_data = {'Date': ['31-Dec','31-Dec','31-Dec','31-Dec','31-Dec'],
          'ID': ['0001','0002','0003','0004', '0006'],
          'Value' : [100.00, 200.00, 300.00, 400.00, 600.00],
          'Category' : ['A','B','C','E','D'],
          'Subcategory' : ['A100','B101','C300','E900','D900']}

prior_df = pd.DataFrame(prior_data)
current_df = pd.DataFrame(current_data)

# Method 1 - df.compare
# https://sparkbyexamples.com/pandas/pandas-difference-between-two-dataframes/
print ("#1 - df.compare") 
print ( prior_df.compare( current_df ) )
'''
     Date            ID        Value        Category       Subcategory      
     self   other  self other   self  other     self other        self other
0  30-Nov  31-Dec   NaN   NaN    NaN    NaN      NaN   NaN         NaN   NaN
1  30-Nov  31-Dec   NaN   NaN    NaN    NaN      NaN   NaN        B120  B101
2  30-Nov  31-Dec   NaN   NaN    NaN    NaN      NaN   NaN         NaN   NaN
3  30-Nov  31-Dec   NaN   NaN  450.0  400.0        D     E        D900  E900
4  30-Nov  31-Dec  0005  0006  500.0  600.0      NaN   NaN         NaN   NaN
'''

# Method 2
# https://stackoverflow.com/questions/70578236/python-pandas-compare-two-dataframes-in-multiple-ways-by-custom-id
def get_only_left(df1, df2):
    left_merge = pd.merge(df1, df2, on='ID', suffixes=('', '_other'), how='left')
    added_columns = [c + '_other' for c in df1.columns if c != 'ID']
    mask = left_merge.loc[:, added_columns].isna().all(axis=1)
    return left_merge[mask].drop(added_columns, axis=1)

diff_df = pd.concat([get_only_left(prior_df, current_df), get_only_left(current_df, prior_df)])
print("#2 .merge")
print("  #2a one side only:")
print(diff_df)

columns = list(current_df.columns)
df = pd.merge(current_df, prior_df, on='ID', suffixes=('', '_prior'), how='inner')
mask = df['Value'] != df['Value_prior']
df[mask].loc[:, columns + ['Value_prior']]

'''
     Date    ID  Value Category Subcategory
4  30-Nov  0005  500.0        D        D900
4  31-Dec  0006  600.0        D        D900
'''
#...


# Method 3 - dataframe-diff
'''
Refer: https://pypi.org/project/dataframe-diff/
install: `pip install dataframe-diff`
'''
d1_column,d2_additional=dataframe_diff(prior_df, current_df, key=['ID'])

print ('#3 dataframe-diff')

print( '  #3a diff column')
print( d1_column)
'''
     ID value_x value_y  column_name
0  0001  30-Nov  31-Dec         Date
1  0002  30-Nov  31-Dec         Date
2  0002    B120    B101  Subcategory
3  0003  30-Nov  31-Dec         Date
4  0004  30-Nov  31-Dec         Date
5  0004   450.0   400.0        Value
6  0004    D900    E900  Subcategory
7  0004       D       E     Category
'''

print( '  #3b addition row')
print( d2_additional)
'''
     Date    ID  Value Category Subcategory  sets
0  30-Nov  0005  500.0        D        D900  df_x
1  31-Dec  0006  600.0        D        D900  df_y
'''