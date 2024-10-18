import pandas as pd
import json

# https://www.geeksforgeeks.org/python-pandas-dataframe-to-nested-json/
# https://likegeeks.com/pandas-dataframe-to-nested-json/


# Create a sample DataFrame
data = {
    'CustomerID': [1, 2, 3, 4],
    'Region': ['East', 'West', 'East', 'West'],
    'Plan': ['Basic', 'Premium', 'Standard', 'Basic'],
    'DataUsage': [2.5, 5.0, 3.5, 2.0]
}
df = pd.DataFrame(data)

# Convert DataFrame to nested JSON
print("df:\n", df)
json_data = df.to_json(orient='records')
print("json:\n", json_data)

'''
    CustomerID Region      Plan  DataUsage
0           1   East     Basic        2.5
1           2   West   Premium        5.0
2           3   East  Standard        3.5
3           4   West     Basic        2.0

json:
 [{"CustomerID":1,"Region":"East","Plan":"Basic","DataUsage":2.5},{"CustomerID":2,"Region":"West","Plan":"Premium","DataUsage":5.0},{"CustomerID":3,"Region":"East","Plan":"Standard","DataUsage":3.5},{"CustomerID":4,"Region":"West","Plan":"Basic","DataUsage":2.0}]
'''

 
# ## group by ##
nested_json = df.groupby('Region').apply(lambda x: x.drop('Region', axis=1).to_dict(orient='records')).to_json()

print('group by Region:\n', nested_json, "\n")

'''
group by Region: 
{"East":[{"CustomerID":1,"Plan":"Basic","DataUsage":2.5},{"CustomerID":3,"Plan":"Standard","DataUsage":3.5}],
 "West":[{"CustomerID":2,"Plan":"Premium","DataUsage":5.0},{"CustomerID":4,"Plan":"Basic","DataUsage":2.0}]}
'''
#print(df.resetindex)



# ## Complex Nesting with Multi-Level Index ##
data = {
    'CustomerID': [1, 1, 2, 2],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb'],
    'DataUsage': [2.5, 3.0, 5.0, 4.5],
    'MinutesUsage': [300, 350, 500, 450]
}
df = pd.DataFrame(data).set_index(['CustomerID', 'Month'])
print("MultiIndex:\n", df, "\n")

nested_json = df.to_json(orient='index')
print("MultiIndex (json):\n", nested_json, "\n")

'''
MultiIndex:
                   DataUsage  MinutesUsage
CustomerID Month                         
1          Jan          2.5           300
           Feb          3.0           350
2          Jan          5.0           500
           Feb          4.5           450 

MultiIndex (json):
 {"(1, 'Jan')":{"DataUsage":2.5,"MinutesUsage":300},"(1, 'Feb')":{"DataUsage":3.0,"MinutesUsage":350},"(2, 'Jan')":{"DataUsage":5.0,"MinutesUsage":500},"(2, 'Feb')":{"DataUsage":4.5,"MinutesUsage":450}} 
 '''


 # https://www.geeksforgeeks.org/python-pandas-dataframe-to-nested-json/

 
# note: str(int) - convert to string 
def custom_nested_structure(row):
    return {  'idx': str(row['CustomerID']) + '-' + row['Month'], 'usage': {'data': row['DataUsage'], 'minutes': row['MinutesUsage']}}

df = df.reset_index()
#print(df)
json_data_custom = df.apply(custom_nested_structure, axis=1).tolist()
json_output = json.dumps(json_data_custom, indent=2)

print(json_output)