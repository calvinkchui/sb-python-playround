var snippets = [
{
  title: "function",  
  syntax: "python",  
  codeUrl: "basic/function.py",
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
}      
]
