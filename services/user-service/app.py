from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob",   "email": "bob@example.com"},
]

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "user-service"})

@app.route('/users')
def get_users():
    return jsonify(users)

@app.route('/users/<int:uid>')
def get_user(uid):
    user = next((u for u in users if u["id"] == uid), None)
    return jsonify(user) if user else (jsonify({"error": "not found"}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
