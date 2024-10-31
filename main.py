from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
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

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

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
        # Handle form submission and user registration (if needed)
        # ...
        return redirect(url_for('index'))

    # Check if user is logged in
    if 'username' in session:
        # Display user-specific content
        return render_template('index.html', form=form, username=session['username'], current_time=datetime.utcnow())
    else:
        # Display general content for non-logged-in users
        return render_template('index.html', form=form, current_time=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Implement authentication logic here (e.g., check against a database)
        if is_valid_user(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Implement is_valid_user function to check user credentials
def is_valid_user(username, password):
    # Replace with your authentication logic (e.g., database lookup)
    return username == 'your_username' and password == 'your_password'  # Replace with actual credentials

if __name__ == '__main__':
    app.run(debug=True)
