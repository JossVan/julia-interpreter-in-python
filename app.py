from flask import Flask, redirect, url_for, render_template, request
from gramatica.gramatica import parse as g
app = Flask(__name__)
import logging
import sys
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
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
        return render_template('principal.html', resultado=result[1], entrada = inpt)

    else:
        return render_template('principal.html')

#reportes
@app.route('/reportes', methods=["GET", "POST"])
def reportes(): 
    return render_template('reportes.html')

@app.route('/AST')
def AST():
    try:
        if result[0] != None:
            return render_template('AST.html', dot = result[0])
        else:
            return render_template('AST.html', dot ="")
    except:
        return render_template('AST.html', dot ="")
@app.route('/TablaSimbolos')
def tabla():
    return render_template('tabla.html', tabla = result[2])

@app.route('/Errores')
def errores():
    return render_template('errores.html', tabla = result[3])
if __name__ == '__main__':
    app.run(debug = True)