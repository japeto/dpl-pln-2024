from flask import Flask, jsonify, request

from loader import model1, model2, model3, model4, model5

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def pong():
  return jsonify({"message": "pong"})

@app.route("/tokenize/<int:alg>", methods=['POST'])
def tokenize(alg):
  text = request.json['text']
  result = {
    1: model1.tokenize(text),
    2: model2.tokenize(text),
    3: model3.tokenize(text),
  }[alg]
  return jsonify({"text": text, "algorithm":alg, "tokenized":result})

@app.route("/stemmeing/<int:alg>/tokenize/<int:tk>", methods=['POST'])
def stemmeing(alg, tk):
  text = request.json['text']
  result = {
    1: model1.tokenize(text),
    2: model2.tokenize(text),
    3: model3.tokenize(text),
  }[tk]
  stemmed = [ [model4.stem(a_token) for a_token in a_sentence] for a_sentence in result]
  return jsonify({"text": text, "algorithm":alg, "tokenized":result, "stemmed": stemmed})

@app.route("/lemmatizer/<int:alg>/tokenize/<int:tk>", methods=['POST'])
def lemmatizer(alg, tk):
  text = request.json['text']
  result = {
    1: model1.tokenize(text),
    2: model2.tokenize(text),
    3: model3.tokenize(text),
  }[tk]

  lemmatized = [ [model5.lemmatize(a_token) for a_token in a_sentence] for a_sentence in result]
  return jsonify({"text": text, "algorithm":alg, "tokenized":result, "lemmatized": lemmatized})



if __name__ == "__main__":
  app.run(debug=True)