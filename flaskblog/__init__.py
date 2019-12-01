from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flaskblog.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt() # for incription and decription
moment = Moment() # for local time on the user posted 
login_manager = LoginManager() # login required
login_manager.login_view = 'users.login' # makes sure that when login required, takes user to login page
login_manager.login_message_category = 'info' # nice bootstrap blue color

mail = Mail()




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  
    bcrypt.init_app(app) # incription and decription
    moment.init_app(app) # local time on the user posted 
    login_manager.init_app(app) # login required
    mail.init_app(app)

    # import applications such as users and then register them with the application
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.handlers.errors import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

