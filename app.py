from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("Inicio.html")

@app.route('/espe')
def espe():
    return render_template("Especializacao.html")

@app.route('/contato')
def contato():
    return render_template("Contato.html")

@app.route('/agendamento')
def agendamento():
    return render_template("Agendamento.html")

@app.route('/dicas')
def dicas():
    return render_template("Dicas.html")

@app.route('/duvidas')
def duvidas():
    return render_template("Duvidas.html")



if __name__ == '__main__':
    app.run()
