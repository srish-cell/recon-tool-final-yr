# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts.nmap import nmapscan
from scripts.dnsenum import dnsenumscan
from scripts.sublist import sublist3r
from scripts.shodan import resolve_domain, lookup_host

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')
    if not target:
        return jsonify({"error": "Target is required"}), 400

    output = nmapscan(target)
    output += dnsenumscan(target)
    s=sublist3r(target)
    output+=s
    output+=lookup_host(resolve_domain(target))
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
