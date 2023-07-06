```python
from openai import GPT
from website.models.Question import Question

class QuestionGenerator:
    def __init__(self):
        self.gpt = GPT()

    def generate_question(self, level):
        prompt = f"Generate a Python question for level {level}"
        response = self.gpt.generate(prompt)
        question_text = response['choices'][0]['text']
        question = Question(question_text, level)
        return question
```