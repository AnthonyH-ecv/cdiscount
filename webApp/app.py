from flask import Flask, request, render_template
from price_parser import parse_price

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        sku = request.form['sku']
        result = parse_price(sku)

        if isinstance(result, str):
            title = result
            return render_template("index.html", title=title)
        else:
            price = result[0]
            title = result[1]
            return render_template("index.html", price=str(price), title=title)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
