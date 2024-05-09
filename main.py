from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', calculo="")

@app.route('/resultado', methods=['POST'])
def calculo():
    numero = 5
    numeros = []
    while numero != 100:
        if (numero %7 == 0) and (numero %5 != 0):
            numeros.append(numero)
        numero += 1
    print(numeros)
    return render_template('index.html', numeros=numeros)

if __name__ == '__main__':
    app.run(debug=True)