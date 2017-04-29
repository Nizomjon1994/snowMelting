from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import desc

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
db.create_all()
engine = create_engine('sqlite:///E:\\Pycharm Projects\\FlaskBlue\\app.sqlite')
# engine = create_engine('sqlite:////var/www/FlaskApp/FlaskApp/app.sqlite')
Session = scoped_session(sessionmaker(bind=engine))

from blue.api.routes import mod
from blue.site.routes import mod

app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api/v1')


