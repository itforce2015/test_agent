```python
import openai

openai.api_key = 'your-openai-api-key'

def generate_prompt(level):
    base_prompt = "Write a Python program that"
    difficulty_prompts = {
        1: "prints 'Hello, World!'",
        2: "calculates the sum of two numbers",
        # ... add more prompts for each level
        50: "implements a complex algorithm"
    }
    return f"{base_prompt} {difficulty_prompts.get(level, 'does something')}."

def generate_question(level):
    prompt = generate_prompt(level)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()
```