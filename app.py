from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

#por default
@app.route('/')
def index():
    return render_template('index.html')
#principal
@app.route('/principal')
def principal():
    return render_template('principal.html')
#reportes
@app.route('/reportes')
def reportes():
    return 'reportes'
if __name__ == '__main__':
    app.run(port = 3000, debug = True)