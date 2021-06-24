# from flask import render_template,redirect,url_for,flash,request
# from ..models import User
# from .forms import RegistrationForm, LoginForm
# from flask_login import login_user
# from .. import db
# from . import auth

# @auth.route('/register',methods = ["GET","POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data,password = form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('auth.login'))
#     return render_template('auth/login.html',registration_form = form)


# @auth.route('/login',methods=['GET','POST'])
# def login():
    
#     login_form = LoginForm()
#     if login_form.validate_on_submit():
#         user = User.query.filter_by(email = login_form.email.data).first()
#         if user is not None and user.verify_password(login_form.password.data):
#             login_user(user,login_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))

#         flash('Invalid username or Password')

#     title = "login"
#     return render_template('auth/login.html',login_form = login_form,title=title)

# from ..models import User
# from .forms import RegistrationForm, LoginForm
# from flask_login import login_user
# from .. import db
# from . import auth

# @auth.route('/register',methods = ["GET","POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data,password = form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('auth.login'))
#     return render_template('auth/login.html',registration_form = form)


# @auth.route('/login',methods=['GET','POST'])
# def login():
    
#     login_form = LoginForm()
#     if login_form.validate_on_submit():
#         user = User.query.filter_by(email = login_form.email.data).first()
#         if user is not None and user.verify_password(login_form.password.data):
#             login_user(user,login_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))

#         flash('Invalid username or Password')

#     title = "login"
#     return render_template('auth/login.html',login_form = login_form,title=title)


from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from .forms import LoginForm, SignupForm
from  .. import db
from ..models import User
from .. import login_manager
from . import auth_bp


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('index'))
        flash('A user already exists with that email address.')
    return render_template('signup.html',title='Create an Account.',form=form,template='signup-page')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_b.login'))

    return render_template('login.html',form=form,title='Log in.',template='login-page')