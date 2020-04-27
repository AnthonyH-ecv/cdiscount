import requests
from bs4 import BeautifulSoup

def parse_price(sku):

        url = 'https://www.cdiscount.com/f-0-'+sku+'.html'
        response = requests.get(url)

        if response.ok:
           soup = BeautifulSoup(response.text, 'html.parser')
           item_price = soup.find(itemprop="price")
           item_title = soup.find(itemprop="name")
           title = item_title.text
           price = float(item_price.attrs['content'])
           return price, title

        else:
           return "Bad request !"