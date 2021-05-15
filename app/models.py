from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    scores = db.relationship('Score',backref='User',lazy='dynamic')
    def setpw(self,password):
        self.password_hash = generate_password_hash(password)
    def checkpw(self, password):
        return check_password_hash(self.password_hash, password)
    def __init__(self, *args, **kwargs):
        self.password_hash = ""
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    attempts = db.Column(db.Integer)

    def __repr__(self):
        return '<score {}>'.format(self.score)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

