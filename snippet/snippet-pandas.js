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
  },{
      title: "Pandas - Get Row", 
      content:`
    * \`at[row name, column name]\`
    * \`iat[row index, column index]\`
    `,
      syntax: "python",  
      codeUrl: "topic/data/pandas_0021_getCell.py",
  },{
    title: "Pandas - Read Excel", 
    syntax: "python",  
    codeUrl: "topic/data/pandas_0100_readEXcel.py",
  },{  
    title: "Pandas - Get Cell", 
    content:`
  * \`loc[row names][column names]\`
  * \`iloc[row indexes][column indexes]\`
  `,
    syntax: "python",  
    codeUrl: "topic/data/pandas_0020_getRow.py",
  }
]
)

