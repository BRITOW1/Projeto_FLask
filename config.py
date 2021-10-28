import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'um-nome-bem-seguro'



#*******************************************************
#CODIGO ANTES DE DAR ERRO NO BANCO DA AULA 10 CRUD
#DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
#SQLALCHEMY_TRACK_MODIFICATIONS = True
#SECRET_KEY = 'um-nome-bem-seguro'
