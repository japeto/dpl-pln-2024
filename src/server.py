from flask import Flask, jsonify, request

from loader import model1, model2, model3 

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def pong():
  return jsonify({"message": "pong"})

@app.route("/tokenize/<int:alg>", methods=['POST'])
def process(alg):
  text = request.json['text']
  result = {
    1: model1.tokenize(text),
    2: model2.tokenize(text),
    3: model3.tokenize(text),
  }[alg]
  return jsonify({"text": text, "algorithm":alg, "tokenized":result})


if __name__ == "__main__":
  app.run(debug=True)