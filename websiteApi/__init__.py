from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import path
# from flask_login import LoginManager
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

def create_app():
    global mongo
    # mongo.init_app(app)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'anhsgret'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/m3sproject'
    mongo = PyMongo(app)
    CORS(app)


    from .AdminDeshboard import AdminDeshboard
    from .Auth import Auth
    from .AdminTaskData import AdminTaskData
    from .allmentee import allmentee
    from .allmentor import allmentor
    from .location import location
    from .BU import Bu
    from .designation import designation
    from .techgroup import techgroup
    from .EmpData import Empdata


    app.register_blueprint(AdminDeshboard,url_prefix='/')
    app.register_blueprint(AdminTaskData,url_prefix='/')
    app.register_blueprint(Auth,url_prefix='/')
    app.register_blueprint(allmentee,url_prifix='/')
    app.register_blueprint(allmentor,url_prifix='/')
    app.register_blueprint(location,url_prifix='/')
    app.register_blueprint(Bu,url_prifix='/')
    app.register_blueprint(designation,url_prifix='/')
    app.register_blueprint(techgroup,url_prifix='/')
    app.register_blueprint(Empdata,url_prifix='/')


    return app