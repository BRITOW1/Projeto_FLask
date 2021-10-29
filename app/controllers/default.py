from flask import render_template, flash, redirect, url_for
from flask.globals import session
from flask.helpers import url_for
from flask_wtf import form
from werkzeug.utils import redirect
from app import app,db, lm
from flask_login import login_required, login_user, logout_user

from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@login_required
#@app.route("/")
def index():
    return render_template('index.html')


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


    


