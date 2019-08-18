from flask_script  import Manager
from flask_migrate import Migrate , MigrateCommand
from app import app 
from app.models import db

manager = Manager(app) #migrations manager for app
migrate = Migrate(app , db) #specifying app to migrate

manager.add_command('db' , MigrateCommand) #command to migrate 


if __name__ == '__main__':
    manager.run() #running manager after migrations



