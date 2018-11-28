from flask import Flask, jsonify, abort, request
from counter import Counter
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'hfa' }
]
ID = Counter()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<id>')
def product(id):
    product_id = int(id)
    for item in PRODUCTS:
            if item['id']  == product_id:
                return jsonify(item)
    abort(404)

@app.route('/api/v1/products/<id>', methods=['DELETE'])
def del_product(id):
    product_id = int(id)
    a = 0
    for item in PRODUCTS:
            if item['id']  == product_id:
                del PRODUCTS[a]
            a += 1
    return '', 204

@app.route('/api/v1/products', methods=['POST'])
def add_product():
    content = request.get_json("name")
    product = {}
    product["id"] = ID.next()
    product["name"] = content["name"]
    PRODUCTS.append(product)
    return jsonify(product), 201

@app.route('/api/v1/products/<id>', methods=['PATCH'])
def update_product(id):
    product_id = int(id)
    content = request.get_json("name")
    a = 0
    for item in PRODUCTS:
            if item['id']  == product_id:
                b = a
                PRODUCTS[a]["name"] = content["name"]
            a += 1
    return jsonify(PRODUCTS[b]), 204
