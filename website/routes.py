```python
from flask import render_template, request, redirect, url_for
from website.app import app
from website.utils.question_generator import generate_question
from website.utils.answer_checker import check_answer
from website.utils.level_generator import generate_level
from website.utils.user_management import manage_user
from website.utils.result_management import update_result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/level', methods=['GET', 'POST'])
def level():
    if request.method == 'POST':
        level = generate_level()
        return redirect(url_for('question', level=level))
    return render_template('level.html')

@app.route('/question/<int:level>', methods=['GET', 'POST'])
def question(level):
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct = check_answer(user_answer)
        update_result(correct)
        return redirect(url_for('result'))
    question = generate_question(level)
    return render_template('question.html', question=question)

@app.route('/result')
def result():
    result = manage_user()
    return render_template('result.html', result=result)
```