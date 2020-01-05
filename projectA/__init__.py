import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

app.config['SECRET_KEY'] = 'sdaw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'aryandb.db')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from .index.routes import index_Blueprint
from .users.routes import users
from .package.routes import package_Blueprint

app.register_blueprint(index_Blueprint)
app.register_blueprint(users)
app.register_blueprint(package_Blueprint)
