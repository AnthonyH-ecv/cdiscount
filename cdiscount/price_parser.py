import requests
from bs4 import BeautifulSoup


def parse_price(sku):

    if isinstance(sku, str):

        url = 'https://www.cdiscount.com/f-0-'+sku+'.html'
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            itemprice = soup.find(itemprop="price")
            price = float(itemprice.attrs['content'])
            return price
        else:
            return response.status.code
    else:
        return "the argument of function isn't a string"
