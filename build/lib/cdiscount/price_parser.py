import requests
from bs4 import BeautifulSoup


def parse_price(sku):

    if isinstance(sku, str):

        url = 'https://www.cdiscount.com/f-0-'+sku+'.html'
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            item_price = soup.find(itemprop="price")

            # if the sku isn't a product id
            if item_price is None:
                return "The sku you entered is not a product identifier"
            else:
                price = float(item_price.attrs['content'])
                return price
        else:
            return response.status.code
    else:
        return "the argument of function isn't a string"
