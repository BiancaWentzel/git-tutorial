// Functions
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
    question: "Was bedeutet die Abkürzung VCS im Zusammenhang mit Git?",
    answers: {
      a: "Verkehrsclub Schweiz",
      b: "Version Controll System",
      c: "Vena cava superior"
    },
    correctAnswer: "b"
  },
  {
    question: "Wodurch zeichnet sich ein VCS aus?",
    answers: {
      a: "Es versioniert unterschiedliche Bearbeitungszustände eines Projektes.",
      b: "Es hilft zur Strukturierung eines Projektes.",
      c: "Es prüft den Code und dessen Syntax."
    },
    correctAnswer: "a"
  },
  {
    question: "Welche zusätzlichen Ebenen werden durch das Initialisieren eines Repsotories angelegt?",
    answers: {
      a: "Working Directory, Staging Area und Respository",
      b: "Repository",
      c: "Staging Area und Respository"
    },
    correctAnswer: "c"
  },
    {
    question: "Was beschreibt das Working Directory im Zusammenhang mit Git",
    answers: {
      a: "Das Arbeitsverzeichnis bzw. Projektverzeichnis, in dem sich alle zum Projekt gehörenden Dateien " +
          "befinden und ein Repsoitory angelegt wurde.",
      b: "Einen Ordner",
      c: "Der Bereich, in dem Änderungen zur Versionierung vorgemert werden."
    },
    correctAnswer: "a"
    },
    {
    question: "Was wäre ein sinnvolles Synonym für die Staging Area?",
    answers: {
      a: "Archiv",
      b: "Anzeigeebene",
      c: "Zwischenablage/ Merkzettel"
    },
    correctAnswer: "c"
    },
    {
    question: "Wie nennt sich die Ebene, in der lokal alle Versionen des Projektes als Snapshot mit Autor " +
        "und Zeistempel abgespeichert werden?",
    answers: {
      a: "Working Area",
      b: "Repository",
      c: "Staging Area"
    },
    correctAnswer: "b"
    },
    {
    question: "Wo trägt man Deteien und Ordner ein, die bei der Versionierung nicht beachtet werden sollen?",
    answers: {
      a: ".git-Verzeichnis",
      b: "main-Datei",
      c: ".gitignore"
    },
    correctAnswer: "c"
    },
    {
    question: "Betrachte folgendes Bild. Was zeigt es? <br><img src='first_picture.png' height='300'/>",
    answers: {
      a: "Dass die Datei datei1.txt als Version ins Respository commited wurde und datei2.txt neu angelegt.",
      b: "Dass die datei datei1.txt zur Versionierung vorgemerkt wurde und datei2.txt neu angelegt.",
      c: "Dass die Dateien datei1.txt und datei2.txt bearbeitet wurden und bisher noch nie zur Versionierung vorgemerkt wurden, " +
          "weil sie neu dazugekommen sind."
    },
    correctAnswer: "b"
    },
    {
    question: "Betrachte folgendes Bild. Was zeigt es? <br><img src='second_picture.png' height='300'/>",
    answers: {
      a: "Die Dateien datei2.txt und datei3.txt wurden verändert, datei1.txt ist zur Archivierung vorgemerkt.",
      b: "Die Dateien datei2.txt und datei3.txt sind neu angelegt, datei1.txt existierte bereits im Projekt und wurde verändert.",
      c: "Die Dateien datei2.txt und datei3.txt sind zur Archivierung vorgemrkt, datei1.txt wurde soeben archiviert."
    },
    correctAnswer: "b"
    },
    {
    question: "Betrachte folgendes Bild. Was zeigt es? <br><img src='third_picture.png' height='300'/>",
    answers: {
      a: "Die Datei datei3.txt wurde verändert, datei2.txt ist zur Archivierung vorgemerkt und Datei1.txt wurde neu angelegt.",
      b: "Die Datei datei3.txt wurde soeben archiviert, datei2.txt ist zur Archivierung vorgemerkt und datei1.txt wurde verändert.",
      c: "Die datei datei3.txt wurde zur Archivierung vorgemerkt, datei2.txt ist neu im Projekt, datei1.txt existierte bereits im Projekt und wurde verändert."
    },
    correctAnswer: "c"
    },
    {
    question: "Welcher Befehl merkt Änderungen zur Versionierung vor?",
    answers: {
      a: "Git status",
      b: "Git add",
      c: "Git commit"
    },
    correctAnswer: "b"
    },
    {
    question: "Welcher Befehl zeigt mir alle veränderten Files im " +
        "Projekt an, egal ob zur Versionierung vorgemerkt oder nicht?",
    answers: {
      a: "Git status",
      b: "Git add",
      c: "Git commit"
    },
    correctAnswer: "a"
    },
    {
    question: "Welcher Befehl legt eine neue Projektversion im Archiv an?",
    answers: {
      a: "Git status",
      b: "Git add",
      c: "Git commit"
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