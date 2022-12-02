from flask import Flask, request
from flask import jsonify
from flask_cors import CORS #include this line
from joblib import dump, load
import json

app = Flask(__name__)
app.run(debug=True)
CORS(app)
# @app.route("/")
# def hello_world():
#     return "<p>Olá mundo</p>"

@app.route('/learn', methods=['POST'])
def learn():
    # Get item from the POST body
    req_data = request.get_json()
    timeHoldDD = req_data[0:-1]
    # timeHoldDD = timeHoldDD.reshape(-1,1)
    user = req_data[-1]
    print(timeHoldDD)
    print(user)
    result = ''
    model = load("./models/"+user+".joblib")
    X_test = [timeHoldDD]
    res = model.predict(X_test)
    res = bool(res)
    #data = jsonify(req_data)
    #req_data = jsonify
    #print(type(data))

    #pegar os modelos treinados para cada classe/usuario, para o usuario entrado verificar se ele é mesmo ele, se der true e se não dar falso, com o predict do classificador ja treinado.
    return str(res)