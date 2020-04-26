from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/',  methods=['GET','POST'])
def home():
    if(request.method == 'POST'):

       sku = request.form['sku']
       url = 'https://www.cdiscount.com/f-0-'+sku+'.html'
       response = requests.get(url)

       if response.ok:
           soup = BeautifulSoup(response.text, 'html.parser')
           item_price = soup.find(itemprop="price")
           item_title = soup.find(itemprop="name")
           title = item_title.text
           price = float(item_price.attrs['content'])
           return render_template('index.html', price=str(price), title=title)

       else:
           return "Bad request !"
    else:
        return render_template('index.html')
