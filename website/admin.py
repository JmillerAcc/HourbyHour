from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, User, Comment
from flask_login import login_required, current_user
from flask import request, url_for, redirect
from datetime import datetime


admin = Admin(name='My App')

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))
    
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Comment, db.session))



from flask import Blueprint, render_template

admin_views = Blueprint('admin_views', __name__)

@admin_views.before_request
@login_required
def reset_last_visit():
    if request.path.startswith('/admin'):
        current_user.last_visit = datetime.utcnow()
        db.session.commit()


def update_banner_text():
    banner_text = "Current banner text"  # Replace with your actual banner text
    if request.method == 'POST':
        new_banner_text = request.form['banner-text']
        # Save the new banner text to your database or wherever you're storing it
        banner_text = new_banner_text
    return ('/admin',banner_text)


