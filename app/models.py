from flask_sqlalchemy import SQLAlchemy
from app import app
from config import ProductionConfig
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login
from datetime import datetime



app.config.from_object(ProductionConfig)
db = SQLAlchemy(app) #adding app to sqlalchemy databaase







class Name(db.Model): #model for database
    id = db.Column(db.Integer , primary_key=True)#we have to specify pk manually
    name =db.Column(db.String(200))
    surname=db.Column(db.String(300))
    age = db.Column(db.Integer)


    def __repr__(self): 
        #this acts like __str__ of django
        return f'<Name {self.name}>'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
 
    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)
 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


