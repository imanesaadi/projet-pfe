from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop",  "price": 999},
    {"id": 2, "name": "Phone",   "price": 499},
    {"id": 3, "name": "Tablet",  "price": 299},
]

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "product-service"})

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/products/<int:pid>')
def get_product(pid):
    product = next((p for p in products if p["id"] == pid), None)
    return jsonify(product) if product else (jsonify({"error": "not found"}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
