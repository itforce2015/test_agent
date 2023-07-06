document.addEventListener('DOMContentLoaded', (event) => {
    const resultContainer = document.querySelector('#result-container');

    function updateResultDisplay(result) {
        resultContainer.innerHTML = '';
        const resultElement = document.createElement('div');
        resultElement.className = 'result';
        resultElement.innerHTML = `
            <h2>Result</h2>
            <p>Level: ${result.level}</p>
            <p>Score: ${result.score}</p>
            <p>Correct Answers: ${result.correctAnswers}</p>
            <p>Incorrect Answers: ${result.incorrectAnswers}</p>
        `;
        resultContainer.appendChild(resultElement);
    }

    function fetchResult() {
        fetch('/api/result')
            .then(response => response.json())
            .then(result => {
                updateResultDisplay(result);
            })
            .catch(error => console.error('Error:', error));
    }

    fetchResult();

    const socket = io();
    socket.on('resultUpdated', fetchResult);
});