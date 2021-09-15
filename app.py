from flask import Flask, redirect, url_for, render_template, request
from gramatica.gramatica import parse as g
import requests
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
        global result
        result =  g(tmp_val+"\n")
        return render_template('principal.html', resultado=result[1])

    else:
        return render_template('principal.html')

#reportes
@app.route('/reportes', methods=["GET", "POST"])
def reportes():
    return render_template('reportes.html')

@app.route('/AST')
def AST():
    return render_template('AST.html', img = result[0])


if __name__ == '__main__':
    app.run(port = 3000, debug = True)