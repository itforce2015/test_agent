1. Exported Variables:
   - `app` (Flask application instance) in `app.py` and `main.py`
   - `db` (Database instance) in `models` files and `user_management.py`, `result_management.py`

2. Data Schemas:
   - `User` schema in `User.py`, `user_management.py`, `result_management.py`
   - `Question` schema in `Question.py`, `question_generator.py`, `answer_checker.py`
   - `Level` schema in `Level.py`, `level_generator.py`
   - `Result` schema in `Result.py`, `result_management.py`

3. DOM Element IDs:
   - `#question-container` in `question.html`, `main.js`, `questions.js`
   - `#level-container` in `level.html`, `main.js`, `levels.js`
   - `#result-container` in `result.html`, `main.js`, `results.js`
   - `#user-info` in `index.html`, `main.js`

4. Message Names:
   - `questionGenerated` in `question_generator.py`, `questions.js`
   - `levelGenerated` in `level_generator.py`, `levels.js`
   - `answerChecked` in `answer_checker.py`, `main.js`
   - `resultUpdated` in `result_management.py`, `results.js`

5. Function Names:
   - `generate_question` in `question_generator.py`, `questions.js`
   - `generate_level` in `level_generator.py`, `levels.js`
   - `check_answer` in `answer_checker.py`, `main.js`
   - `update_result` in `result_management.py`, `results.js`
   - `manage_user` in `user_management.py`, `main.js`

6. Shared Dependencies:
   - Flask in `app.py`, `main.py`, `routes.py`
   - SQLAlchemy in `models` files and `user_management.py`, `result_management.py`
   - OpenAI GPT in `question_generator.py`, `openai_gpt.py`