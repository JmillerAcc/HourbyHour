from flask import Blueprint, flash, request, jsonify
from flask import render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user
from .forms import ResetRequestForm, ResetPasswordForm
from flask_security import Security, SQLAlchemyUserDatastore
from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer
from .models import User
from flask_security.utils import verify_and_update_password, get_token_status
from flask import current_app
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from website import create_app
from website import TIMEZONE


auth = Blueprint('auth', __name__)

@auth.route('/admin')
@login_required
def admin():
    current_user.last_visit = datetime.now(tz=TIMEZONE)
    db.session.commit()
    if current_user.is_admin:
        return render_template('admin.html', user=current_user)
    else:
        return redirect(url_for('views.home'))

@auth.route('/login', methods=['POST','GET'])
def login():
    message = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Log in Success!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Password/Email is incorrect. Please try again.", category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", message=message, user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif not first_name:
            flash('First name is required.', category='error')
        elif len(first_name) < 3:
            flash('First name must be greater than 2 character', category='error')
        elif not last_name:
            flash('Last name is required.', category='error')
        elif len(last_name) < 3:
            flash('Last name must be greater than 2 character', category='error')

        elif password1 != password2:
            flash('Passwords dont\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


def send_mail(user, token_str):
    mail = Mail(current_app)
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = s.dumps({'user_id': user.id, 'token_str': token_str}, salt=current_app.config['SECURITY_PASSWORD_SALT'])
    msg = Message(
        'Password Recovery',
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[user.email]
    )
    link = url_for('auth.passRecover', token=token, _external=True)
    msg.body = f"Hi {user.first_name},\n\nYou can reset your password by clicking on the following link:\n{link}\n\nThe link will expire in {current_app.config['RECOVERY_EXPIRATION']} hours."
    mail.send(msg)
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

@auth.route('/password-recover', methods=["POST", "GET"])
def recover():
    form = ResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Generate a token with the user ID and an expiration time
            s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
            token = s.dumps({'user_id': user.id}, salt=current_app.config['SECURITY_PASSWORD_SALT'])

            # Send the password reset link to the user via email
            send_mail(user, token)

            flash('Reset request sent. Check your email for recovery options.')
            return redirect(url_for('auth.login'))
        else:
            flash("Email does not exist!", category="success")
    return render_template("recover.html", form=form, user=current_user)

@auth.route('/reset-password/<token>', methods=["POST", "GET"])
def passRecover(token):
    form = ResetPasswordForm()
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        # Load the user ID from the token
        data = s.loads(token, salt=current_app.config['SECURITY_PASSWORD_SALT'], max_age=current_app.config['RECOVERY_EXPIRATION'])
        user_id = data['user_id']
        user = User.query.get(user_id)
    except (SignatureExpired, BadSignature):
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('auth.recover'))
    if form.validate_on_submit():
        # Update the user's password in the database
        user.password = generate_password_hash(form.password.data)
        db.session.commit()

        flash('Your password has been reset. Please login with your new password.')
        return redirect(url_for('auth.login'))
    return render_template("reset.html", form=form, user=current_user)




    


    