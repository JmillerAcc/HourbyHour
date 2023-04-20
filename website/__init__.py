from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore
from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail
from flask_migrate import Migrate
from config import TIMEZONE
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from datetime import timedelta




db = SQLAlchemy()
migrate = Migrate()
DB_NAME = 'database1.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mySecret'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=60)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECURITY_PASSWORD_SALT'] = 'password-salt'
    app.config['SECURITY_RECOVERABLE'] = True
    app.config['SECURITY_TRACKABLE'] = True
    app.config['MAIL_SERVER'] = 'mail.accuridecorp.com'
    app.config['MAIL_PASSWORD']= None
    app.config['MAIL_PORT'] = 25
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = None
    app.config['MAIL_DEFAULT_SENDER'] = 'noreply@accuridecorp.com'
    app.config['RECOVERY_EXPIRATION'] = 24
    app.config['TIMEZONE'] = TIMEZONE     
    mail = Mail(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .views import views
    from .auth import auth
    from .admin import admin_views



    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin_views, url_prefix='/admin')


    class NotificationView(BaseView):
        @expose('/')
        def index(self):
            return self.render('admin/notify.html')


    
    from .models import User, Note, Comment

    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    # Create admin object
    admin = Admin(app, name='My App', template_mode="bootstrap4")
    class CommentAdminView(ModelView):
        column_list = ('id', 'lineNumber', 'dayOfWeek', 'timestamp', 'subject', 'comment', 'user_id')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Note, db.session))
    admin.add_view(CommentAdminView(Comment, db.session))
    admin.add_view(NotificationView(name='Notifications', endpoint='notify'))
    
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
    print("created database")