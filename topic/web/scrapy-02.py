import scrapy

'''
* Extract Data
  - `response.css("title")` : List of `Selector`
  - `response.css("title::title").getall()` : extract text
  - `response.css("title::title").get()` : first result
  - `response.css("title::text").re(r"Quotes.*")`: use with `re` 
* Shell
```
> scrapy shell 'https://www.zyte.com/blog/page/1'
response.css(".oxy-post .oxy-post-title ")
[<Selector query="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post ')]/descendant-or-self::*/*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post-title ')]" data='<a class="oxy-post-title" href="/blog...'>, <Selector query="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post ')]/descendant-or-self::*/*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post-title ')]" data='<a class="oxy-post-title" href="/blog...'>, <Selector query="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post ')]/descendant-or-self::*/*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post-title ')]" data='<a class="oxy-post-title" href="/blog...'>, <Selector query="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post ')]/descendant-or-self::*/*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post-title ')]" data='<a class="oxy-post-title" href="/blog...'>, <Selector query="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' oxy-post ')]
...
```
'''


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = [
        'https://www.zyte.com/blog/',
        'https://www.zyte.com/blog/page/2/'
    ]

    def parse(self, response):
                
        
        for title in response.css('.oxy-post'):
        
            print ("URL: " + response.request.url)
            
            yield {
            'title': title.css('.oxy-post-title ::text').get(),
            'date': title.css('.oxy-post-image-date-overlay ::text').get()
              .strip() # remove white space
            }
            

						