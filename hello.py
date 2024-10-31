from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import request

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return render_template('user.html', name=name, prontuario=prontuario, instituicao=instituicao)

@app.route('/contexto_requisicao/<name>')
def contexto_requisicao(name, navegador=None, ip=None, host=None):
    navegador = request.user_agent.browser
    ip = request.remote_addr
    host = request.host

    return render_template('contexto_requisicao.html', name=name, navegador=navegador, ip=ip, host=host)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
