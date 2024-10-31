from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

disciplina_choices = [
    ('DSWA5', 'DSWA5'),
    ('DWBA4', 'DWBA4'),
    ('Gestão de Projetos', 'Gestão de Projetos'),
]

class NameForm(FlaskForm):
    name = StringField('Informe o seu Nome: *', validators=[DataRequired()])
    last_name = StringField('Informe o seu sobrenome: *', validators=[DataRequired()])
    instituicao = StringField('Informe a sua Instituição de Ensino: *', validators=[DataRequired()])
    disciplina = SelectField('Informe a sua Disciplina: *', choices=disciplina_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_last_name = session.get('last_name')
        if old_name is not None and old_name != form.name.data:
            flash('Parece que você trocou de nome!')
        if old_last_name is not None and old_last_name != form.last_name.data:
            flash('Parece que você trocou de sobrenome!')
        session['name'] = form.name.data
        session['last_name'] = form.last_name.data
        session['instituicao'] = form.instituicao.data
        session['disciplina'] = form.disciplina.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), last_name=session.get('last_name'), instituicao=session.get('instituicao'), disciplina=session.get('disciplina'), current_time=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['nome']
        return redirect(url_for('loginResponsive', name=usuario))
    return render_template('login.html',
                           current_time=datetime.utcnow())

@app.route('/login-responsive/<name>', methods=['GET'])
def loginResponsive(name):
    usuario=name
    return render_template('login_responsive.html', usuario=usuario,current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)

