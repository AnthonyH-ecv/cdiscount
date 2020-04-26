Cdiscount package 
===================
Un package Python capable de relever le prix  de n'importe quel produit 
du site www.cdiscount.com

Vous pouvez l'installer avec pip:

    pip install cdiscount

Exemple d'usage:

    >>> from cdiscount.price_parser import parse_price
    >>>
    >>> sku = "del5397184246030"   # product identifier
    >>>
    >>> parse_price(sku)
    >>> 1776.6

Ce code est sous licence <a href="https://en.wikipedia.org/wiki/GNU_General_Public_License">GPL V3</a>.