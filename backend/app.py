# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts.nmap import nmapscan

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')
    if not target:
        return jsonify({"error": "Target is required"}), 400

    output = nmapscan(target)
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
