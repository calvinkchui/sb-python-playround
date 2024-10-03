snippets = snippets.concat(
[
  {
    title: "Pandas - Basic", 
    content:`
  Strcuture:
  * \`Series\`: Column
  * \`DataFrame\`: Table
  
  Read Data:
  * [Read CSV](https://www.w3schools.com/python/pandas/pandas_csv.asp)
    * \`pd.read_csv('data.csv')\`
  * [Read JSON](https://www.w3schools.com/python/pandas/pandas_json.asp)
  
  Analying Data:
  * \`df.head(10)\` -  return first 10 rows of the DataFrame
  * \`df.tail()\` -  return last 5 rows of the DataFrame
  * \`df.info()\` - Information of data
  `,
    syntax: "python",  
    codeUrl: "topic/data/pandas_0010_basic.py",
  }, {
      title: "Pandas - Dropping", 
      content:`
    \`\`\`
    s.drop(['x']) # drop value from rows (axis=0)
    df.drop("calories", axis=1) # drop value from column(axis=1)
    \`\`\`
    `,
      syntax: "python",  
      codeUrl: "topic/data/pandas_0012_dropping.py",
  
  },{
    title: "Pandas - Data Frame - Join", 
    syntax: "python",  
    content:`
Syntex:
\`\`\`
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None)
\`\`\`

* \`how\`:  left, right, outer, inner, cross

* Refer [Join](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)

`,
    codeUrl: "topic/data/pandas_0018_df-join.py",    
  },{  
    title: "Pandas - DataFrame - rename", 
    content:`
Syntex:
\`\`\`pyhton    
DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, copy=None, inplace=False, level=None, errors='ignore')
\`\`\`

* [rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
`,
    syntax: "python",  
    codeUrl: "topic/data/pandas_0020_getRow.py",    
  },{  
    title: "Pandas - DataFrame - Get Row", 
    content:`
    * \`loc[row names]\`
    * \`iloc[row indexes]\`    
  `,
    syntax: "python",  
    codeUrl: "topic/data/pandas_0020_getRow.py",
  },{  
    title: "Pandas - Get Cell", 
    syntax: "python",  
    content: `
* \`loc[row names][column names]\`
* \`iloc[row indexes][column indexes]\`
* \`at[row name, column name]\`
* \`iat[row index, column index]\`
         
\`\`\`python
df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})

print(df.iloc[0][0]) # 1
print(df.loc[0]['A']) # 1
print(df.at[0,'A']) # 1
print(df.iat[0,0]) # 1
\`\`\`    

Refer [DataFrame](https://www.datacamp.com/tutorial/pandas-tutorial-dataframe-pythonp)
`,
    codeUrl: "topic/data/pandas_0021_getCell.py",
  },{
    title: "Pandas - Dataframe.groupBy", 
    syntax: "python",  
    codeUrl: "topic/data/pandas_0030_df-groupBy.py",   
    content: `
  
  \`\`\`python
  df.groupBy(by=["key"]).agg( {'col': func}) )
  \`\`\`    
  `    
  },{    
    title: "Pandas - Change Value by condition", 
    syntax: "python",  
    codeUrl: "topic/data/pandas_0090_df-case-changeValueByCondition.py",   
    content: `

\`\`\`python
# Using dataframe.loc[] Function
df.loc[ df["column_name"] == "some_value", "column_name"] = "value"

# Using np.where() Function
df["column_name"] = np.where(df["column_name"]=="some_value", value_if_true, value_if_false)

# Using masking
df["column_name"].mask( df["column_name"] == "some_value", value , inplace=True )

# Using apply() Function and lambda
df['gender'] = df['gender'].apply(lambda x: 0 if x == 'female' else x)
\`\`\`    
`
  },{
    title: "Pandas - Read Excel", 
    syntax: "python",  
    codeUrl: "topic/data/pandas_0100_readExcel.py",
  }
]
)

