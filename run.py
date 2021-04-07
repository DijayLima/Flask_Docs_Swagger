from os import environ
from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

from routes import api as home_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app, title='Api Flask Expieriments', version='1.0', description='Api de experimentos com python flask',prefix='/api')

#adicionado namespace pessoa para rotas
api.add_namespace(home_ns, path='/funcionario')

if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host=SERVER_HOST,port=5500, debug=(not environ.get('ENV') == 'PRODUCTION'),threaded=True)