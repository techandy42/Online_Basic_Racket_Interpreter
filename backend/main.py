import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from Run import Run
from config import outputs
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_root():
  response = jsonify({'message': 'This is the Basic Racket Interpreter server.'})
  return response

@app.route('/', methods=['POST'])
def main():
  data = json.loads(request.data)
  input = data['input']
  show_steps = data['show_steps']
  result = Run.run(input, show_steps)

  response = jsonify({'result': result, 'outputs': outputs})
  return response