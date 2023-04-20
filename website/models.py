from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from config import TIMEZONE
from datetime import datetime
from pytz import timezone




class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    is_superuser = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    current_line = db.Column(db.Integer)
    is_assigned_to_line = db.Column(db.Boolean, default=False)
    last_visit = db.Column(db.DateTime(timezone=True), default=datetime.now(tz=TIMEZONE))

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_superuser': self.is_superuser,
            'is_admin': self.is_admin,
            'current_line': self.current_line,
            'is_assigned_to_line': self.is_assigned_to_line,
            'last_visit': self.last_visit.isoformat()
        }

    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineNumber = db.Column(db.Integer)
    dayOfWeek = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now(tz=TIMEZONE))
    subject = db.Column(db.String(100))
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.first_name'))
    user = db.relationship('User', backref=db.backref('comment', lazy=True))
    downTimeType = db.Column(db.String(50))

    def __repr__(self):
        return f"Comment('{self.lineNumber}', '{self.dayOfWeek}', '{self.subject}', '{self.comment}', '{self.user_id}', '{self.downTimeType}')"
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()


class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'date_created': self.date_created.isoformat()
        }