from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user , login_required , logout_user ,login_user
from projectA import db , bcrypt
from projectA.forms import Register_form, Login_form
from projectA.models import User


users = Blueprint('users', __name__)


@users.route('/register', methods=['POST', 'GET'])
def register_view():
    if current_user.is_authenticated:
        return redirect(url_for('index_Blueprint.index'))

    form = Register_form()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            email=form.email.data,
            password=pw_hash,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login_view'))

    return render_template('register.html', form=form,log_reg_title='Create An Account')


@users.route('/login', methods=['POST', 'GET'])
def login_view():
    if current_user.is_authenticated:
        return redirect(url_for('index_Blueprint.index'))
    form = Login_form()
    if form.validate_on_submit():
        db_user = User.query.filter_by(email=form.email.data).first()
        if bcrypt.check_password_hash(db_user.password ,form.password.data):
            login_user(db_user)
            return redirect(url_for('index_Blueprint.index'))

    return render_template('login.html', form=form , log_reg_title='Login To Your Account')


@users.route('/logout')
@login_required
def logout_view():
    logout_user()
    return redirect(url_for('index_Blueprint.index'))
