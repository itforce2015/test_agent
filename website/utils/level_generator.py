```python
from website.models.Level import Level
from website.models.Question import Question
from website.utils.question_generator import generate_question

def generate_level(level_number):
    level = Level.query.filter_by(number=level_number).first()
    if not level:
        level = Level(number=level_number)
    
    questions = []
    for i in range(level_number):
        question = generate_question(level_number)
        questions.append(question)
    
    level.questions = questions
    return level
```