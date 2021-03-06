from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False          

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email): #Inicializar
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<Post %r>"%self.username


class Motivos(db.Model):
    __tablename__ = "motivos"

    codigo = db.Column(db.String, primary_key = True)
    macro = db.Column(db.String)
    micro = db.Column(db.String)
    explicacao = db.Column(db.String)
    exemplo = db.Column(db.String)
    page = db.Column(db.String)

    def __init__(self, codigo, macro, micro, explicacao, exemplo, page):
        self.codigo = codigo
        self.macro = macro
        self.micro = micro
        self.explicacao = explicacao
        self.exemplo = exemplo
        self.page = page
    
    def __repr__(self):
        return self.codigo
        
#class Post(db.Model):
#    __tablename__ = "posts"
#    id= db.Column(db.Integer, primary_key = True)
#    content = db.Column(db.Text)
#    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#    user = db.relationship('User',foreign_keys=user_id)
    
#    def __init__(self, content,user_id):
#        self.content = content
#        self.user_id = user_id
        
#    def __repr__(self):
#        return "<Post %r>"%self.id 

#class Follow(db.Model):
#    __tablename__ = "follow"
#    id = db.Column(db.Integer, primary_Key = True)
#    user_id = db.Column(db.Integer, db.foreignKey('users.id'))
#    follower_id = db.Column(db.Integer, db.foreignKey('users.id'))

#    user = db.relationship('User',foreign_keys=user_id)
#    follower = db.relationship('User',foreign_keys=follower_id)

#db.create_all()
#db.session.commit()
