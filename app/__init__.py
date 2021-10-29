from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, migrate
from flask_login import LoginManager
import sqlite3


app = Flask(__name__)
app.config.from_object('config')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

lm = LoginManager()
lm.init_app(app)


from app.models import tables
from app.controllers import default


