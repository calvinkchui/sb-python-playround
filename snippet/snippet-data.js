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
    title: "String",
    syntax: "python",
    codeUrl: "basic/string.py"
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
    title: "module",
    content: `
* Define Module, file named mymodule.py:
def helloWorld():
 ...
    
import mymodule
mymodule.helloWorld() 

* Re-naming a moudle
import mymodule as mx
mx.mymodule()

`    
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
  title: "Asset",
  content: `
* syntex "assert exp1", raise AssertError of assert result is false
* for DEv test error only. Not for runtime   
`
},
/*
{
  title: "Context Manager",
  content: `
* example
\`\`\`pyhton
with open('test.txt', 'w' as f: // close f after execute the block
  f.write("Test!") 
\`\`\`

* Implement object support ``with``
\`\`\`python
Class Demo:
  def __init__(self):
     ..
  def __enter__(self): // code with 
     ..
  def __exist__(self, exc_type, exc_vale, traceback): // exit code with
     ..

with Demo() as x:
   ...
\`\`\`
`
},
*/
{
  title: "variable naming",
  content: `
* \`_var\`: reminder developer it is private variable. Reminder developer don't access outside the object.
* \`var_\`: avoid conflict with reserved word
* \`__var\`: private variable. Python will rename the variable interally.
* \`__var__\` : Pyhton reservice method
* \`_\` : temp variable
`
},


{
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
