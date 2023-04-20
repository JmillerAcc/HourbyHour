from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .models import User, Comment


from packages import l471_df, l474_df, l424_df, l429_df, l458_df



app = Flask(__name__, template_folder='templates', static_folder='static')

views = Blueprint('views', __name__)


def get_last_comment():
    return Comment.query.filter_by(user_id=current_user.first_name + ' ' + current_user.last_name).order_by(Comment.id.desc()).first()


from website import TIMEZONE
from datetime import datetime

def get_new_comment_count():
    last_visit = current_user.last_visit  

    if last_visit is None:  # if the user is visiting for the first time, return total comment count
        return Comment.query.count()
    else:
        new_comments = Comment.query.filter(Comment.timestamp > last_visit).count()
        return new_comments


@views.route('/')
@login_required
def home():
    return render_template("index.html", user=current_user)

@views.route('/reset_new_comment_count', methods=['POST'])
@login_required
def reset_new_comment_count():
    current_user.last_visit = datetime.now(tz=TIMEZONE)
    db.session.commit()
    return redirect(url_for('views.profile'))

@views.route('/474', methods=['GET', 'POST'])
@login_required
def l_474():
    if request.method == 'POST':
        lineNumber = request.form.get('lineNumber')
        dayOfWeek = request.form.get('dayOfWeek')
        subject = request.form.get('subject')
        comment = request.form.get('comment')
        downTimeType = request.form.get('downtimeType')  # Get the selected downtime type
        user_id = current_user.first_name + ' ' + current_user.last_name  # add a space between first name and last name
        new_comment = Comment(lineNumber=lineNumber, dayOfWeek=dayOfWeek, subject=subject, comment=comment, user_id=user_id, downTimeType=downTimeType)
        db.session.add(new_comment)
        try:
            db.session.commit()
            flash('Comment saved successfully', category="success")
        except:
            db.session.rollback()
            flash('Failed to save comment', category="error")
    
    return l474_df()

  

@views.route('/471', methods=['GET', 'POST'])
@login_required
def l_471():   
    if request.method == 'POST':
        lineNumber = request.form.get('lineNumber')
        dayOfWeek = request.form.get('dayOfWeek')
        subject = request.form.get('subject')
        comment = request.form.get('comment')
        user_id = current_user.first_name + ' ' + current_user.last_name  # add a space between first name and last name
        new_comment = Comment(lineNumber=lineNumber, dayOfWeek=dayOfWeek, subject=subject, comment=comment, user_id=user_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment saved successfully', 'success')
    return l471_df()

@views.route('/424', methods=['GET', 'POST'])
@login_required
def l_424():
    if request.method == 'POST':
        lineNumber = request.form.get('lineNumber')
        dayOfWeek = request.form.get('dayOfWeek')
        subject = request.form.get('subject')
        comment = request.form.get('comment')
        user_id = current_user.first_name + ' ' + current_user.last_name  # add a space between first name and last name
        new_comment = Comment(lineNumber=lineNumber, dayOfWeek=dayOfWeek, subject=subject, comment=comment, user_id=user_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment saved successfully', 'success')
    return l424_df()

@views.route('/429', methods=['GET', 'POST'])
@login_required
def l_429():
    if request.method == 'POST':
        lineNumber = request.form.get('lineNumber')
        dayOfWeek = request.form.get('dayOfWeek')
        subject = request.form.get('subject')
        comment = request.form.get('comment')
        user_id = current_user.first_name + ' ' + current_user.last_name  # add a space between first name and last name
        new_comment = Comment(lineNumber=lineNumber, dayOfWeek=dayOfWeek, subject=subject, comment=comment, user_id=user_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment saved successfully', 'success')
    return l429_df()

@views.route('/458', methods=['GET', 'POST'])
@login_required
def l_458():
    if request.method == 'POST':
        lineNumber = request.form.get('lineNumber')
        dayOfWeek = request.form.get('dayOfWeek')
        subject = request.form.get('subject')
        comment = request.form.get('comment')
        user_id = current_user.first_name + ' ' + current_user.last_name  # add a space between first name and last name
        new_comment = Comment(lineNumber=lineNumber, dayOfWeek=dayOfWeek, subject=subject, comment=comment, user_id=user_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment saved successfully', 'success')
    return l458_df()

@views.route('/461', methods=['GET', 'POST'])
@login_required
def menu461():
    return render_template("461.html", user= current_user)







from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from flask import current_app, url_for
from .models import User
from flask_mail import Mail

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if request.form.get('reset_form'):
            current_password = request.form.get('password')
            new_password = request.form.get('new_password')
            confirm_new_password = request.form.get('confirm_new_password')
            if new_password and confirm_new_password:
                if check_password_hash(current_user.password, current_password):
                    if check_password_hash(current_user.password, new_password):
                        flash('Your new password cannot be the same as your old password', 'error')
                    elif new_password != confirm_new_password:
                        flash('Passwords do not match', category='error')
                    else:
                        current_user.password = generate_password_hash(new_password)
                        db.session.commit()
                        flash('Your password has been reset', 'success')
                else:
                    flash('Current password is incorrect', 'error')
            else:
                flash('Please enter both new password and confirmation password', 'error')
        elif request.form.get('message'):
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            send_mail(name, email, message)
            flash("Message sent! Thank you for contacting us.", category="success")
        else:
            flash("All fields are required.", category="error")
    last_comment = get_last_comment()
    new_comments = get_new_comment_count()
    
    return render_template('profile.html', last_comment=last_comment, user=current_user, new_comments=new_comments)


def send_mail(name, email, message):
    admins = User.query.filter_by(is_admin=True).all()
    if not admins:
        return
    mail = Mail(current_app)
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    for admin in admins:
        token = s.dumps(admin.email, salt=current_app.config['SECURITY_PASSWORD_SALT'])
        msg = Message(
            'New Contact Form Submission',
            sender=current_user.email,
            recipients=[admin.email]
        )
        msg.body = f"Hi {admin.first_name},\n\nA new message has been submitted from the contact form:\n\nName: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)



@views.route("/get_updated_data")
def get_updated_data():
  # Call your l429_df function to get the updated data
  updated_data = l429_df()
  # Return the updated data in JSON format
  return jsonify({"data": updated_data})



