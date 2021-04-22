from flask import Flask, request, jsonify
from model import predict_test

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return jsonify({'prediction': predict_test})


@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({'results': 1})
