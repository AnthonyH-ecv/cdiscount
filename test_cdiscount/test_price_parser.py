import unittest
from cdiscount.price_parser import parse_price

class TestParsePrice(unittest.TestCase):

    def test_parse_price(self):
        sku = "del5397184246030"
        price = parse_price(sku)

        if self.assertIsInstance(sku , str):
            self.assertIsInstance(price, float)

if __name__ == '__main__':
    unittest.main()