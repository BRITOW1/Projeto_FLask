from typing import AsyncContextManager
from flask import render_template, flash, redirect, url_for,request,Response, jsonify
from flask.globals import session
from flask.helpers import url_for
from flask_wtf import form
from sqlalchemy.orm import query
from werkzeug.utils import redirect
from app import app,db, lm
from flask_login import login_required, login_user, logout_user
from wtforms import TextField, Form

from app.models.tables import Motivos
from app.models.tables import User
from app.models.forms import LoginForm

#15h20
import json 
import os   

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = SearchForm(request.form)
    return render_template('index.html')

#def teste():
#    form = SearchForm(request.form)
#    return render_template("teste.html", form=form)



@app.route("/", methods = ["GET","POST"])
@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login realizado com sucesso!")
            return redirect(url_for("index"))
        else:
            flash("Acesso não autorizado!")
    return render_template('login2.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("login"))

@app.route('/produtoErrado')
@login_required
def produtoErrado():
    return render_template('produtoErrado.html')

@app.route('/arrependimento')
@login_required
def arrependimento():
    return render_template('arrependimento.html')

@app.route('/problemaEntraga')
@login_required
def problemaEntraga():
    return render_template('problemaEntraga.html')

@app.route('/compraErrada')
@login_required
def compraErrada():
    return render_template('compraErrada.html')
    
@app.route('/pagamento')
@login_required
def pagamento():
    return render_template('pagamento.html')

@app.route('/embalagem')
@login_required
def embalagem():
    return render_template('embalagem.html')

@app.route('/escolhas')
@login_required
def escolhas():
    return render_template('escolhas.html')

@app.route('/reconhecimento')
@login_required
def reconhecimento():
    return render_template('reconhecimento.html')

@app.route('/resposta/<codigo>')
@login_required
def resposta(codigo):
    str(codigo)
    resposta = Motivos.query.filter_by(codigo=codigo).first_or_404(description='There is no data with {}'.format(codigo))
    return render_template('resposta.html',post=resposta)

@app.route('/listagem')
@login_required
def listagem():
    lista = []
    listagem = Motivos.query.all()
    for list in listagem:
        lista.append(list)
    return render_template('listagem2.html', post=listagem)

@app.route('/buscar/<name>')
@login_required
def buscar(name):
    micro = []
    macro = []
    desc = []

    macro4 = "%{}%".format(name)

    rMi = Motivos.query.filter(Motivos.micro.like(macro4)).all()
    for mi in rMi:
        micro.append(mi)
    
    rMa = Motivos.query.filter(Motivos.macro.like(macro4)).all()
    aMa = "zero"
    for ma in rMa:
        if ma.macro != aMa:
            macro.append(ma)        
        aMa = ma.macro
        # macro.append(ma)

    rDs = Motivos.query.filter(Motivos.explicacao.like(macro4)).all()
    for exp in rDs:
        desc.append(exp)   
        
    return render_template('buscar2.html', micro=micro, macro=macro, desc=desc)


#*********************
class SearchForm(Form):
    autocomp = TextField('', id='procurar')
    

# @app.route('/_autocomplete', methods=['GET'])
# def autocomplete():
#     with open("names.json", 'r', encoding='utf8') as f:   
#         cities = json.load(f)
#         f.close()
#         # print(cities)
#     return Response(json.dumps(cities), mimetype='application/json')

@app.route('/procurar')
def autocomplete():
    query = request.args.get('query')
    with open("Motivos.json", "r", encoding='utf8') as f:
        cities = json.load(f)
        f.close()
        print(cities)
        return jsonify({"suggestions":cities})


