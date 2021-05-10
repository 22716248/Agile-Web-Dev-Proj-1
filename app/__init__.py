from flask import Flask
<<<<<<< HEAD
from flask import render_template
=======
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

>>>>>>> parent of 46946aa (Basic flask)
app = Flask(__name__)

<<<<<<< HEAD
from app import routes
=======
from app import routes, models
>>>>>>> parent of 46946aa (Basic flask)
