```python
from website.models.Question import Question

def check_answer(question_id, user_answer):
    question = Question.query.get(question_id)
    if not question:
        return False, "Question not found"

    correct_answer = question.answer
    if user_answer == correct_answer:
        return True, "Correct answer"
    else:
        return False, "Incorrect answer"
```