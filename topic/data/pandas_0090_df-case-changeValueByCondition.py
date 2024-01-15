import numpy as np
import pandas as pd

# copy from https://www.geeksforgeeks.org/how-to-replace-values-in-column-based-on-condition-in-pandas/

Student = {
    'Name': ['John', 'Jay', 'sachin', 'Geetha', 'Amutha', 'ganesh'],
    'gender': ['male', 'male', 'male', 'female', 'female', 'male'],
    'math score': [50, 100, 70, 80, 75, 40],
    'test preparation': ['none', 'completed', 'none', 'completed',
                         'completed', 'none'],
}


# Example
print('#1 Using dataframe.loc[] Function')
df = pd.DataFrame(Student)
df.loc[df["gender"] == "male", "gender"] = np.NaN
print(df)


print('#2 Using np.where() Function')
df = pd.DataFrame(Student)
df["gender"] = np.where(df["gender"] == "female", 0, 1)
print(df)


print('#3 Using masking')
df = pd.DataFrame(Student)
df['gender'].mask(df['gender'] == 'female', 0, inplace=True)

print(df)


print('#4 Using apply() Function and lambda')
df = pd.DataFrame(Student)
df['gender'] = df['gender'].apply(lambda x: 0 if x == 'female' else x)
print(df)



# More example -Trim and change blank to NaN 
print('#4-1 Trim and change blank to NaN')
Student = {
    'Name': ['John', 'Jay', 'sachin', 'Geetha', 'Amutha', 'ganesh'],
    'remarks': ['', np.NaN, ' ', 'completed', 'completed', 'completed'],
    'remarks2': ['', np.NaN, ' ', '  ', 'space   ', 'completed'],
}

df = pd.DataFrame(Student)
df_obj = df.select_dtypes(['object']) # get Column in type object(String)

df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip()).replace('', np.nan) 
    # x.str.strip() - tirm
    # replace('', np.nan) - '' to NaN
print(df)