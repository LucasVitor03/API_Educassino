from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

#@app.route("/contador", methods=['POST'])
#def counter():
    global click_count
    click_count += 1
    return jsonify({'click_cout': click_count}) 

#@app.route("/mostrarcontador", methods=['GET'])
#def counter_show():
    return jsonify({'click_count': click_count})


if __name__ == '__main__':
    app.run(debug=True)
    #port=5000

    #API de verdade - Receberia a informações do nosso JS e faria os cálculos e retornar na página index.html


    app = Flask(__name__)

    #aqui ficaria o calculo de porcentagem de cada jogada
    #faz um GET dos dados do banco MongoBD e depois um POST no HTML

    if __name__ == '__main__':
        app.run(debug=True, port=5500)