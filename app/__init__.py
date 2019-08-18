from flask import Flask
from flask_login import LoginManager

#create app
app = Flask(__name__) #init app
app.config['SECRET_KEY'] = 'any string works here'

#register login
login = LoginManager(app)
login.init_app(app)


login.login_view = 'user.login' #redirect users to login view if they are not logged in


# register blueprints
from .user import user as user_blueprint
app.register_blueprint(user_blueprint)

from app import views #importing views 

views.app #running views



