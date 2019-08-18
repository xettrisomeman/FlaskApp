from flask import Blueprint #importing blueprint
 
user = Blueprint('user', __name__,template_folder='templates',static_folder='static') #using blueprint



from . import views





