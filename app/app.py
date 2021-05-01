from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api', methods=['GET', 'POST'])
def main():
    user_input = []
    if request.method == 'GET':
        return jsonify({'api': 'welcome to the api'}), 200
    # Iterate through user response and add to prediction value array.
    for key in request.get_json():
        user_input.append(request.get_json()[key])
    showpred = predict(user_input).tolist()
    if request.method == 'POST':
        return jsonify({'prediction': showpred}), 201
