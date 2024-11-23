from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from flask_cors import CORS
import random
import threading

client = MongoClient("mongodb://root:senha123@localhost:27017/")
db = client["feedback"]
collection = db["frases"]

# API principal
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    return render_template('./index.html')

def run_app():
    app.run(port=5000)

app2 = Flask(__name__)
CORS(app2)

jogadas_historico = []

@app2.route('/jogada', methods=['POST'])
def jogada():
    simbolos = ["🍌", "🍎", "🐯", "🐍", "🦁​"]
    total_simbolos = len(simbolos)
    total_combinacoes = total_simbolos ** 3
    combinacoes_vencedoras = total_simbolos
    probabilidade_vitoria = (combinacoes_vencedoras / total_combinacoes) * 100
    probabilidade_perda = 100 - probabilidade_vitoria

    frases = list(collection.find())  # Busca todas as frases
    if frases:
        frase_aleatoria = random.choice(frases).get("texto", "Nenhuma frase encontrada")
    else:
        frase_aleatoria = "Nenhuma frase disponível no momento."

    resultado = random.choices(
        ["Vitória", "Derrota"],
        weights=[probabilidade_vitoria, probabilidade_perda],
        k=1
    )[0]

    jogadas_historico.append({
        'resultado': resultado,
        'frase': frase_aleatoria
    })

    lucro_cassino = probabilidade_perda / 100

    return jsonify({
        'probabilidade': probabilidade_vitoria,
        'resultado': resultado,
        'frase': frase_aleatoria,
        'lucro_cassino': lucro_cassino
    })

@app2.route('/historico', methods=['GET'])
def historico():
    return jsonify(jogadas_historico)

@app2.route('/simulacao', methods=['POST'])
def simulacao():
    dados = request.get_json()
    rodadas = dados.get('rodadas', 100)
    aposta = dados.get('aposta', 1)

    simbolos = ["🍌", "🍎", "🐯", "🐍", "🦁​"]
    total_simbolos = len(simbolos)
    total_combinacoes = total_simbolos ** 3
    combinacoes_vencedoras = total_simbolos
    probabilidade_vitoria = (combinacoes_vencedoras / total_combinacoes)
    probabilidade_perda = 1 - probabilidade_vitoria

    ganhos_jogador = 0
    perdas_jogador = 0

    for _ in range(rodadas):
        if random.random() < probabilidade_vitoria:
            ganhos_jogador += aposta
        else:
            perdas_jogador += aposta

    lucro_cassino = perdas_jogador - ganhos_jogador

    return jsonify({
        'rodadas': rodadas,
        'ganhos_jogador': ganhos_jogador,
        'perdas_jogador': perdas_jogador,
        'lucro_cassino': lucro_cassino
    })

def run_app2():
    app2.run(port=5500)

if __name__ == '__main__':
    threading.Thread(target=run_app).start()
    threading.Thread(target=run_app2).start()
