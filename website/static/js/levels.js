const levelContainer = document.querySelector('#level-container');

function generate_level(level) {
    fetch(`/api/level/${level}`)
        .then(response => response.json())
        .then(data => {
            levelContainer.innerHTML = '';
            data.questions.forEach(question => {
                const questionElement = document.createElement('div');
                questionElement.textContent = question.text;
                levelContainer.appendChild(questionElement);
            });
        })
        .catch(error => console.error('Error:', error));
}

document.addEventListener('levelGenerated', (event) => {
    generate_level(event.detail.level);
});