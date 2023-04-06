import urllib.request 
 
url = "https://fchart.github.io/life.html"
response = urllib.request.urlopen(url)
contents = response.read()
print(contents.decode())
response.close()

