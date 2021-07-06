from flask import render_template, session, redirect, flash, url_for

from app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        print(login_form.username.data)
        username = login_form.username.data
        session['username'] = username
        flash('Registrado con éxito!', category='is-primary is-light')
        return redirect(url_for('index'))

    return render_template('login.html', **context)

## END