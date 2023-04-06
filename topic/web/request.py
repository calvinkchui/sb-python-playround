import requests

url = "https://fchart.github.io/test.html"
response = requests.get(url)
if response.status_code == 200:
  print(response.text)
  print("encoding: ", response.encoding)
else:
  print("Error!")
