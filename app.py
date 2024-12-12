from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    nombre = "Angel"
    Licenciaturas = ["ISC", "LIME", "ARQ", "PSI", "ANI"]
    return render_template('index.html', nombre=nombre, Licenciaturas=Licenciaturas, len=len(Licenciaturas))