function buildQuiz(){
    // variable to store the HTML output
      const output = [];

      // for each question...
      myQuestions.forEach(
        (currentQuestion, questionNumber) => {

          // variable to store the list of possible answers
          const answers = [];

          // and for each available answer...
          for(letter in currentQuestion.answers){

            // ...add an HTML radio button
            answers.push(
              `<label>
                <input type="radio" name="question${questionNumber}" value="${letter}">
                ${currentQuestion.answers[letter]}
              </label><br>`
            );
          }

          // add this question and its answers to the output
          output.push(
            `<div class="block"><div class="question"> ${currentQuestion.question} </div>
            <div class="answers"> ${answers.join('')}</div></div>`
          );
        }
      );

      // finally combine our output list into one string of HTML and put it on the page
      quizContainer.innerHTML = output.join('');
}
function showResults() {

    const output = [];

    // gather answer containers from our quiz
    const answerContainers = quizContainer.querySelectorAll('.answers');

    // keep track of user's answers
    let numCorrect = 0;

    // for each question...
    myQuestions.forEach((currentQuestion, questionNumber) => {

        // find selected answer
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;

        // if answer is correct
        if (userAnswer === currentQuestion.correctAnswer) {
            // add to the number of correct answers
            numCorrect++;

            // color the answers green
            answerContainers[questionNumber].style.background = '#9ccc9c';
        }
        // if answer is wrong or blank
        else {
            // color the answers red
            answerContainers[questionNumber].style.background = '#ffb9b9';
        }
    });
    var newDate = new Date();
    var dateString = newDate.toDateString();
    var timeString = newDate.toLocaleTimeString();

    output.push(`<div class="modal-content">
            <p id="modalcontent" style="font-size:14pt; font-weight:bold;">Geschafft!</p>
            <p>Du hast <span style="font-weight:bold; color: #6b9e1f;">${numCorrect}/${myQuestions.length}</span> Fragen korrekt beantwortet!</p>
            <p>${dateString} ${timeString}</p>
            <p style="color:red;">Vergiss nicht, einen Screenshot hiervon zu machen!</p>
          </div>`);
    modal.innerHTML = output.join('');
    modal.style.display = "block";
}

// Variables
const quizContainer = document.getElementById('quiz');
const submitButton = document.getElementById('submit');
const myQuestions = [
  {
    question: "Mit welchem Befehl füge ich eine Änderung zur Staging area hinzu?",
    answers: {
      a: "git status",
      b: "git add",
      c: "git commit"
    },
    correctAnswer: "b"
  },
  {
    question: "Welcher Befehl versioniert alle vorgemerkten Änderungen?",
    answers: {
      a: "git status",
      b: "git add",
      c: "git commit"
    },
    correctAnswer: "c"
  },
  {
    question: "Mit welchem Befehl zeigt man den Versionierungsstatus der Änderungen an?",
    answers: {
      a: "git status",
      b: "git add",
      c: "git commit"
    },
    correctAnswer: "a"
  },
    {
    question: "Wozu dient der Befehl 'git diff'?",
    answers: {
      a: "Man kann sich den Status der Versionierungen ansehen.",
      b: "Es zeigt die Veränderungen in einer Datei im Vergleich zum letzten Commit an.",
      c: "Man kann den Inhalt von Dateien ansehen."
    },
    correctAnswer: "b"
    },
    {
    question: "Was zeigt 'git log'?",
    answers: {
      a: "Den Inhalt des Archivs",
      b: "Eine Zeitreihe aller gemachten Änderungen",
      c: "Eine Zeitreihe aller gemachten Commits mit Autor, Zeitstempel und Commit-Message."
    },
    correctAnswer: "c"
    },
    {
    question: "Mit welchem Befehl mache ich Änderungen rückgängig, die noch nicht vorgemerkt sind?",
    answers: {
      a: "git reset",
      b: "git checkout",
      c: "git reset --soft",
      d: "git reset --hard"
    },
    correctAnswer: "b"
    },
    {
    question: "Mit welchem Befehl lösche ich einen Commit komplett?",
    answers: {
      a: "git reset",
      b: "git checkout",
      c: "git reset --soft",
      d: "git reset --hard"
    },
    correctAnswer: "d"
    },
    {
    question: "Mit welchem Befehl mache ich einen Commit rückgängig und behalte die Änderungen?",
    answers: {
      a: "git reset",
      b: "git checkout",
      c: "git reset --soft",
      d: "git reset --hard"
    },
    correctAnswer: "c"
    },
    {
    question: "Mit welchem Befehl kann man zum Commit vorgemerkte Änderungen rückgängig machen?",
    answers: {
      a: "git reset",
      b: "git checkout",
      c: "git reset --soft",
      d: "git reset --hard"
    },
    correctAnswer: "a"
    },
    {
    question: "Was macht dieser Befehl: 'git reset --soft HEAD~5'?",
    answers: {
      a: "Man macht 5 Änderungen rückgängig, die zur Versionierung vorgemerkt sind.",
      b: "Man stellt den Commit wieder her, der sich 5 Commits vor dem aktuellen befindet. Hierbei werden alle anderen Änderungen gelöscht.",
      c: "Man stellt den Commit wieder her, der sich 5 Commits vor dem aktuellen befindet. Hierbei werden alle anderen Änderungen beibehalten."
    },
    correctAnswer: "c"
    },
    {
    question: "Was macht der Befehl 'git clone'?",
    answers: {
      a: "Man kopiert den aktuellen Stand des Remote Repositorys ins lokale Repository.",
      b: "Er kopiert das Remote Repository und legt ein lokales Repository mit dem gleichen Inhalt an.",
      c: "Er kopiert ein lokales Repository."
    },
    correctAnswer: "b"
    },
    {
    question: "Wie kopiere ich den Inahlt und die Commit-History des lokalen Repositorys ins Remote Repository.",
    answers: {
      a: "git pull",
      b: "git push",
      c: "git log"
    },
    correctAnswer: "b"
    },
    {
    question: "Wie kopiere ich den Inahlt und die Commit-History des Remote Repositorys ins lokale Repository.",
    answers: {
      a: "git pull",
      b: "git push",
      c: "git log"
    },
    correctAnswer: "a"
    },
    {
    question: "Was ist ein Mergekonflikt?",
    answers: {
      a: "Ein Fehler im Code, der zu Problemen führt.",
      b: "Unterschiedlcihe Versionen von Dateien, die gemerged werden.",
      c: "Verschieden Änderungen an Dateien und Strukturen in einem Projekt, die von git nicht automatisch zusammengeführt werden können."
    },
    correctAnswer: "c"
    }
];

const modal = document.getElementById("myModal");

// Kick things off
buildQuiz();

// Event listeners
submitButton.addEventListener('click', showResults);


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}