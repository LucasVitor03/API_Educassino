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