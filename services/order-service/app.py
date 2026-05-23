from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []
next_id = 1

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "order-service"})

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    global next_id
    data = request.get_json()
    order = {"id": next_id, "user_id": data["user_id"], "product_id": data["product_id"], "status": "pending"}
    orders.append(order)
    next_id += 1
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
