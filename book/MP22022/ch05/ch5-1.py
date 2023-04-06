from urllib.parse import urlparse
 
o = urlparse("http://example.com:80/test/index.php?user=hueyan")
print("通訊協定: ", o.scheme)
print("網域名稱: ", o.netloc)
print("通訊埠號: ", o.port)
print("網頁路徑: ", o.path)
print("查詢字串: ", o.query)
