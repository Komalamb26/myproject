from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

# ✅ Home route (fixes "/" 404)
@app.route('/')
def home():
    return "Product API is running successfully!"

# ✅ GET all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# ✅ ADD product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data:
        return "Invalid input", 400

    products.append(data)
    return jsonify({"message": "Product added", "data": data})

# ✅ UPDATE product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    if id >= len(products):
        return "Product not found", 404

    products[id] = request.get_json()
    return jsonify({"message": "Product updated", "data": products[id]})

# ✅ DELETE product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    if id >= len(products):
        return "Product not found", 404

    deleted = products.pop(id)
    return jsonify({"message": "Product deleted", "data": deleted})

# ✅ Run server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
def list_routes():
    print("\nAvailable API Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.methods} -> http://127.0.0.1:5000{rule}")

if __name__ == '__main__':
    list_routes()
    app.run(port=5000, debug=True)