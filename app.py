from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    Licenciaturas = ["GGHT", "AGRO", "CP", "PSI", "ANI"]
    return render_template('index.html', Licenciaturas=Licenciaturas, len=len(Licenciaturas))