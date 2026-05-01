from flask import Flask, redirect
import random

app = Flask(__name__)

edge_servers = [
    "http://localhost:5000",
    "http://localhost:5001",
    "http://localhost:5002"
]

@app.route('/content/<path:path>')
def balance(path):
    server = random.choice(edge_servers)
    return redirect(f"{server}/content/{path}")

@app.route('/')
def home():
    return "Load Balancer Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)