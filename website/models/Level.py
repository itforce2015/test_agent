from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from website.models import db

class Level(db.Model):
    __tablename__ = 'levels'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    difficulty = Column(String(50), nullable=False)
    questions = relationship('Question', backref='level', lazy=True)

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def __repr__(self):
        return f'<Level {self.name}>'