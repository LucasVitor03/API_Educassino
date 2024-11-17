from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import threading # import para usar 2 api

#Essa API é só para retornar a Página html
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

#API2 - Receberia a informações do nosso JS e faria os cálculos e retornar na página index.html

app2 = Flask(__name__)
CORS(app2)

@app2.route('/')
def home_app2():
    return "API 2 - Porta 5500"

def run_app():
    app.run(port=5000)

def run_app2():
    app2.run(port=5500)

#faz um GET dos dados do banco MongoBD e depois um POST no HTML

if __name__ == '__main__':
    threading.Thread(target=run_app).start()
    threading.Thread(target=run_app2).start()