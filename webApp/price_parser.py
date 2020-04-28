import requests
from bs4 import BeautifulSoup


def parse_price(sku):

    url = 'https://www.cdiscount.com/f-0-'+sku+'.html'
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        item_price = soup.find(itemprop="price")
        item_title = soup.find(itemprop="name")

        # if the sku isn't a product id
        if item_price is None:
            return "The sku you entered is not a product identifier"
        else:
            price = item_price.attrs['content']
            title = item_title.text
            return price, title
    else:
        return "Bad request !"