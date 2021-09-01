from flask import Flask, redirect, url_for, render_template, request
from gramatica.gramatica import parse as g
app = Flask(__name__)

#por default
@app.route('/')
def index():
    return render_template('index.html')
#principal
@app.route('/principal',methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        inpt = request.form['codigo']
        global tmp_val
        tmp_val=inpt
        result = g(tmp_val)
        return render_template('principal.html', resultado=result)
    else:
        return render_template('principal.html')

#reportes
@app.route('/reportes')
def reportes():
    return 'reportes'


if __name__ == '__main__':
    app.run(port = 3000, debug = True)