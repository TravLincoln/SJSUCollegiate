from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from myapp import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True, index=True)
    password = db.Column(db.String(128))
    notes = db.relationship('Note', backref='author', lazy = 'dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    timespam = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.id}: {self.content}>'

class todo_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    todo_item = db.Column(db.String(256))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return self.todo_item

class flash_cards(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    secure_filename = db.Column(db.String)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
