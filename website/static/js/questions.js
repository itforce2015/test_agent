const questionContainer = document.querySelector('#question-container');

// Event listener for question generation
document.addEventListener('questionGenerated', (event) => {
    const question = event.detail;
    displayQuestion(question);
});

// Function to display question
function displayQuestion(question) {
    questionContainer.innerHTML = '';
    const questionElement = document.createElement('p');
    questionElement.textContent = question.text;
    questionContainer.appendChild(questionElement);

    question.answers.forEach((answer, index) => {
        const answerElement = document.createElement('button');
        answerElement.textContent = answer.text;
        answerElement.addEventListener('click', () => checkAnswer(index));
        questionContainer.appendChild(answerElement);
    });
}

// Function to check answer
function checkAnswer(answerIndex) {
    const event = new CustomEvent('answerChecked', { detail: answerIndex });
    document.dispatchEvent(event);
}

// Function to request a new question
function generateQuestion() {
    fetch('/generate_question')
        .then(response => response.json())
        .then(question => {
            const event = new CustomEvent('questionGenerated', { detail: question });
            document.dispatchEvent(event);
        });
}

// Generate the first question when the page loads
generateQuestion();