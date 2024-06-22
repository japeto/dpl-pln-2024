from flask import Flask, jsonify, request
from flask_cors import CORS

from preproces_nltk import preprocessing as pnltk
from preproces_spacy import preprocessing as pspacy

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=['GET'])
def pong():
  return jsonify({"message":"pong"})

@app.route("/preprocessing/<method>", methods=['POST'])
def preprocessing(method):
  text= request.json['text']
  return jsonify({
    1:pnltk(text),
    2:pspacy(text)
  }[method])
