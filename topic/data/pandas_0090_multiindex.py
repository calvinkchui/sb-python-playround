import pandas as pd

# https://www.programiz.com/python-programming/pandas/multiindex

# create a dictionary

data = {
    "Continent": ["North America", "Europe", "Asia", "North America", "Asia", "Europe", "North America", "Asia", "Europe", "Asia"],
    "Country": ["United States", "Germany", "China", "Canada", "Japan", "France", "Mexico", "India", "United Kingdom", "Nepal"],
    "Population": [331002651, 83783942, 1439323776, 37742154, 126476461, 65273511, 128932753, 1380004385, 67886011, 29136808]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

print("# Original:")
print(df)
print("\n\n")




import pandas as pd

# create a dictionary
data = {
    "Continent": ["North America", "Europe", "Asia", "North America", "Asia", "Europe", "North America", "Asia", "Europe", "Asia"],
    "Country": ["United States", "Germany", "China", "Canada", "Japan", "France", "Mexico", "India", "United Kingdom", "Nepal"],
    "Population": [331002651, 83783942, 1439323776, 37742154, 126476461, 65273511, 128932753, 1380004385, 67886011, 29136808]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

# sort the data by continent
df.sort_values('Continent', inplace=True)

# create a multiindex
df.set_index(['Continent','Country'], inplace=True)

print("# Create MultiIndex in Pandas:")
print(df)
print("\n\n")


# https://sparkbyexamples.com/pandas/pandas-multiindex-dataframe-examples/
# create MultiIndex 
  # for Index
multi_index = pd.MultiIndex.from_tuples([("r0", "rA"),
                                       ("r1", "rB")],
                                       names=['Courses','Fee'])

  # for column
cols = pd.MultiIndex.from_tuples([("Gasoline", "Toyoto"), 
                                  ("Gasoline", "Ford"), 
                                  ("Electric", "Tesla"),
                                  ("Electric", "Nio")])  

data=[[100,300, 900,400 ], [200,500, 300,600]]                                                                       

df = pd.DataFrame(data, columns=cols,index=multi_index)
print("from_tuples:\n", df, "\n")


'''
from_tuples:
             Gasoline      Electric     
              Toyoto Ford    Tesla  Nio
Courses Fee                            
r0      rA       100  300      900  400
r1      rB       200  500      300  600 
'''

print("   to json:\n", df.to_json(), "\n")
'''
 {"('Gasoline', 'Toyoto')":{"('r0', 'rA')":100,"('r1', 'rB')":200},"('Gasoline', 'Ford')":{"('r0', 'rA')":300,"('r1', 'rB')":500},"('Electric', 'Tesla')":{"('r0', 'rA')":900,"('r1', 'rB')":300},"('Electric', 'Nio')":{"('r0', 'rA')":400,"('r1', 'rB')":600}} 
'''




  # for column
cols = pd.MultiIndex.from_tuples([("Gasoline", "Toyoto"), 
                                  ("Gasoline", "Ford"), 
                                  ("Electric", "Tesla"),
                                  ("Electric", "Nio")])  

data=[[100, 300, 900,400 ], [200, 500, 300,600]]                                                                       

df = pd.DataFrame(data, columns=cols)
print("test data:\n", df, "\n")
print("   to json:\n", df.to_json(), "\n")

'''
test data:
   Gasoline      Electric     
    Toyoto Ford    Tesla  Nio
0      100  300      900  400
1      200  500      300  600 

   to json:
 {"('Gasoline', 'Toyoto')":{"0":100,"1":200},
  "('Gasoline', 'Ford')":{"0":300,"1":500},
  "('Electric', 'Tesla')":{"0":900,"1":300},
  "('Electric', 'Nio')":{"0":400,"1":600}} 
'''