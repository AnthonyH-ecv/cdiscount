import unittest
from cdiscount.price_parser import parse_price


class TestParsePrice(unittest.TestCase):

    def test_parse_price_sku_is_not_string(self):
        sku = 52545625
        price = parse_price(sku)

        self.assertEqual(price, "the argument of function isn't a string")

    def test_parse_price_sku_is_not_product_id(self):
        sku = "000000"
        price = parse_price(sku)

        self.assertEqual(price,
        "The sku you entered is not a product identifier")

    def test_parse_price_return_float(self):
        sku = "del5397184246030"
        price = parse_price(sku)

        if self.assertIsInstance(sku, str):
            self.assertIsInstance(price, float)

if __name__ == '__main__':
    unittest.main()
