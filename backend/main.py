#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from Run import Run
from config import outputs
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_root():
    return jsonify({'message': 'This is the Basic Racket Interpreter server.'})

@app.route('/', methods=['POST'])
def main():
  data = json.loads(request.data)
  input = data['input']
  show_steps = data['show_steps']
  result = Run.run(input, show_steps)

  return jsonify({'result': result, 'outputs': outputs})

app.run()