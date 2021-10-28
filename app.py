from flask import Flask, render_template
# from flask_login import LoginManager

app = Flask(__name__)

# lm = LoginManager(app)

@app.route('/')
def login():
    return render_template('loign.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/produtoErrado')
def produtoErrado():
    return render_template('produtoErrado.html')

@app.route('/arrependimento')
def arrependimento():
    return render_template('arrependimento.html')

@app.route('/problemaEntraga')
def problemaEntraga():
    return render_template('problemaEntraga.html')

@app.route('/compraErrada')
def compraErrada():
    return render_template('compraErrada.html')

# @app.route('/home')
# def index():
#     return render_template('index.html')

# @app.route('/home')
# def index():
#     return render_template('index.html')

if __name__ == "__main__":
	app.run()