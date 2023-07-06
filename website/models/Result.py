from flask_sqlalchemy import SQLAlchemy
from website.models.User import User
from website.models.Level import Level
from website.models.Question import Question

db = SQLAlchemy()

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)

    user = db.relationship('User', backref=db.backref('results', lazy=True))
    level = db.relationship('Level', backref=db.backref('results', lazy=True))
    question = db.relationship('Question', backref=db.backref('results', lazy=True))

    def __init__(self, user_id, level_id, question_id, is_correct):
        self.user_id = user_id
        self.level_id = level_id
        self.question_id = question_id
        self.is_correct = is_correct