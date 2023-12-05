var snippets = [
  {
    title: "Varible",  
    syntax: "python",  
    codeUrl: "basic/var.py",
  },
  {
    title: "function",  
    syntax: "python",  
    codeUrl: "basic/function.py",
  },
  {
    title: "function - map(), filter(), reduce()",  
    syntax: "python",  
    codeUrl: "basic/function_mapFilterReduce.py",
  },
  {
    title: "io",  
    syntax: "python",  
    codeUrl: "basic/io.py",
  },  
  {
    title: "json",  
    syntax: "python",  
    codeUrl: "basic/pyjson.py",
  }, 
  {
    title: "logging",  
    syntax: "python",  
    codeUrl: "advance/log.py",
  },
  {
    title: "decorator",  
    syntax: "python",  
    codeUrl: "advance/decorator.py",
  },
{
  title: "requests", 
  syntax: "python",  
  code:`# Get
response = request.get(url)
print('body', response.text)

# Post
response = request.post(url, { field:value })

# Session
session = requests.Session() 
session.get(url)
`,
  codeUrl: "topic/web/request.py",
},    
{
  title: "BeautifulSoup", 
  content:`
* [BeautifulSoup Doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Functions:
* [select/select_one](book/MP22022/ch05/ch5-4-3.py") - CSS selector
* [find/find_all](book/MP22022/ch05/ch5-4-3a.py") - find tag
`,
  syntax: "python",  
  codeUrl: "topic/web/bs4.py",
},
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
  codeUrl: "topic/data/pandas_01_basic.py",
},{
  title: "PyTest", 
  content:`
# Pytest
* File start / end with \`test\`
* Class start with \`test\`
* Method start with \'test\'

# Run
\`\`\`py
pytest
pytest test_func.py
\`\`\`
`,
  syntax: "python",  
  codeUrl: "topic/test/test_example.py",  
}
]
