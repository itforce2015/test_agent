```python
from sqlalchemy import Column, Integer, String, Text
from website.models import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    level = Column(Integer, nullable=False)
    question_text = Column(Text, nullable=False)
    correct_answer = Column(String(255), nullable=False)
    wrong_answers = Column(String(255), nullable=False)

    def __init__(self, level, question_text, correct_answer, wrong_answers):
        self.level = level
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers
```