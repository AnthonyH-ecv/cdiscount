import requests
from bs4 import BeautifulSoup

def parse_price(sku) :

    url = 'https://www.cdiscount.com/f-0-'+sku+'.html'
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find(itemprop="price")
        p = float(price.attrs['content'])
        return p