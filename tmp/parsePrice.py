import requests
from bs4 import BeautifulSoup





def getFirstMerchantPrice(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #div.quote-price-normal > div.quote-price-hong > a > span.product-price
    #  <span class="product-price"><span class="text-price-unit">HK$</span><span class="text-price-number" data-price="9950.0">9,950</span></span>

    #tags = soup.select("span.product-price > .text-price-number")
    #tag = tags[0]
    #print("price: ", tag['data-price'])


    #print("tag: ", tag)

    #print("name: ", tag.select('.quotation-merchant-name a')[0].text)

    rst = {}

    '''
    <h1 class="product-name" title="Samsung 三星 Galaxy Z Fold5 5G (12+512GB)">Samsung 三星 Galaxy Z Fold5 5G (12+512GB)
                                                            <span class="discontinued"></span>
                                                        </h1>
    '''
    rst['title'] = soup.find('h1', attrs={"class": "product-name"})['title']

    tags = soup.select(".clearfix > .item-inner")
    tag = tags[0]
    # tag.select('.text-price-number'): [<span class="text-price-number" data-price="9950.0">9,950</span>, <span class="text-price-number" data-price="9550.0">9,550</span>]
    rst['name'] = tag.find("p", attrs={"class": "quotation-merchant-name"} ).find("a").text
    
    
    rst['price'] =tag.select('.text-price-number')[0]['data-price']

    
    
    return rst;

def testRun():
    rst = getFirstMerchantPrice(url = "https://www.price.com.hk/product.php?p=594865") # Fold 5 512
    print(rst)  
    rst = getFirstMerchantPrice(url = "https://www.price.com.hk/product.php?p=594860") # Fold 5 256
    print(rst)  

testRun()