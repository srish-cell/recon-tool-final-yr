# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from scripts.nmap import nmapscan
from scripts.dnsenum import dnsenumscan
from scripts.sublist import sublist3r
from scripts.shodan import resolve_domain, lookup_host
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai

app = Flask(__name__)
CORS(app)
GEMINI_API_URL = "https://api.gemini.com/v1/analyze"

GEMINI_API_KEY = "AIzaSyDC4S2ykQO2yP62_nNe-bHiaB4gp-xA0A0"
genai.configure(api_key="AIzaSyCB3Fs49MnzQRQkh1izebk0hcCqqadjEKc")

generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

)

chat_session = model.start_chat(
  history=[]
)
def analyze(input_code):
    
    response = chat_session.send_message(input_code+"\nAnalyze the given input and  generate a report it in the form of assets found, ip addresses,domains,all data found, vulnerbility , impact and  mitigation" ,safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE

    }
    )
   
    return response.text
@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')
    if not target:
        return jsonify({"error": "Target is required"}), 400

    output = nmapscan(target)
    output += dnsenumscan(target)
    s=sublist3r(target)
    output+=s
    output=lookup_host(resolve_domain(target))
    gemini_report = analyze(output)
    return jsonify({"output":gemini_report})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
