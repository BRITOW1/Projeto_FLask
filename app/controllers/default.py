from flask import render_template, flash, redirect, url_for,request, jsonify,Response
from flask.globals import session
from flask.helpers import url_for
from flask_wtf import form
from werkzeug.utils import redirect
from app import app,db, lm
from flask_login import login_required, login_user, logout_user
from wtforms import TextField, Form
import os.path

from app.models.tables import User
from app.models.forms import LoginForm

#15h20
import json 
import os   

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = SearchForm(request.form)
    return render_template('index.html',form=form)

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
    return render_template('login.html', form=form)


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


#*********************
class SearchForm(Form):
    autocomp = TextField('', id='city_autocomplete')
    

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    # path = r'names.json'
    with open("names.json", 'r', encoding='utf8') as f:   
        cities = json.load(f)
        f.close()
        print(cities)
    return Response(json.dumps(cities), mimetype='application/json')

