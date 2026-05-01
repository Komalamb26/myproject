from flask import Flask, send_file
import os
import sys

app = Flask(__name__)

port = int(sys.argv[1])   # port from command line

@app.route('/content/<path:path>')
def serve_content(path):
    file_path = os.path.join("content", path)
    return send_file(file_path)

@app.route('/')
def home():
    return f"Edge Server Running on Port {port}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)