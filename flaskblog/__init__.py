from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '044c16e09c56ad89a1e136f98ebd0fcc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) # for incription and decription
moment = Moment(app) # for local time on the user posted 
login_manager = LoginManager(app) # login required
login_manager.login_view = 'login' # makes sure that when login required, takes user to login page
login_manager.login_message_category = 'info' # nice bootstrap blue color
app.config['MAIL_SERVER'] = 'stmtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '*****@gmail.com' # needs to fill in real email or set up environment variables
app.config['MAIL_PASSWORD'] = '*********'  # needs to fill in real email or set up environment variables
mail = Mail(app)

from flaskblog import routes
