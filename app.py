from flask import Flask, redirect, url_for, render_template, request
from gramatica.gramatica import parse as g
import requests
import base64
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
    if request.method =="POST":
        
        valor = request.form['btn']
        if valor == "ast":
            return render_template('AST.html')
  
    return render_template('reportes.html')

@app.route('/AST')
def AST():
    return render_template('AST.html', img = result[0])

@app.route('/TablaSimbolos')
def tabla():
    return render_template('tabla.html', tabla = result[2])

if __name__ == '__main__':
    app.run(port = 3000, debug = True)