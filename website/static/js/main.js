```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const userInfo = document.querySelector('#user-info');
    const questionContainer = document.querySelector('#question-container');
    const levelContainer = document.querySelector('#level-container');
    const resultContainer = document.querySelector('#result-container');

    function updateUI() {
        manage_user(userInfo);
        generate_level(levelContainer);
        generate_question(questionContainer);
        update_result(resultContainer);
    }

    updateUI();

    document.addEventListener('questionGenerated', (event) => {
        const question = event.detail;
        questionContainer.innerHTML = question.text;
    });

    document.addEventListener('levelGenerated', (event) => {
        const level = event.detail;
        levelContainer.innerHTML = `Level: ${level.number}`;
    });

    document.addEventListener('answerChecked', (event) => {
        const isCorrect = event.detail;
        if (isCorrect) {
            alert('Correct answer!');
        } else {
            alert('Incorrect answer. Try again!');
        }
    });

    document.addEventListener('resultUpdated', (event) => {
        const result = event.detail;
        resultContainer.innerHTML = `Score: ${result.score}`;
    });
});
```