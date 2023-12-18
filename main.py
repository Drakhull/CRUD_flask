from flask import Flask
from flask.templating import render_template
from flask.helpers import url_for
from flask_migrate import Migrate
from database import db
from users import users_bp
from datetime import datetime


app = Flask(__name__)

conection = 'sqlite:///banco.sqlite'

app.config['SECRET_KEY'] = 'testando-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conection
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(users_bp, url_prefix = '/users')

migrate = Migrate(app, db)

@app.route('/')
def index():
  return render_template('main_page.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
