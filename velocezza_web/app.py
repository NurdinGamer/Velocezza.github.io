from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

# Sample data for products
products = [
    {'name': 'MIDNIGHT CRUISE TSHIRT', 'price': '175.000', 'image': 'tshirt.jpg', 'url': 'www.tokopedia.com/velocezza/midnight-cruise-tshirt-velocezza'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def display_products():
    return render_template('products.html', products=products)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)

