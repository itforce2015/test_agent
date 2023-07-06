```python
from website.models.Result import Result
from website.models.User import User
from website.models.Level import Level
from website.models.Question import Question
from website import db

def update_result(user_id, level_id, question_id, is_correct):
    user = User.query.get(user_id)
    level = Level.query.get(level_id)
    question = Question.query.get(question_id)

    if not user or not level or not question:
        return None

    result = Result.query.filter_by(user_id=user_id, level_id=level_id, question_id=question_id).first()

    if not result:
        result = Result(user_id=user_id, level_id=level_id, question_id=question_id, is_correct=is_correct)
        db.session.add(result)
    else:
        result.is_correct = is_correct

    db.session.commit()

    return result

def get_results(user_id):
    results = Result.query.filter_by(user_id=user_id).all()
    return results

def get_level_results(user_id, level_id):
    results = Result.query.filter_by(user_id=user_id, level_id=level_id).all()
    return results
```