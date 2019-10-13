// select all elements
const start = document.getElementById("start");
const quiz = document.getElementById("quiz");
const question = document.getElementById("question");
const qImg = document.getElementById("qImg");
const qAud = document.getElementById("qAud");
const choiceA = document.getElementById("A");
const choiceB = document.getElementById("B");
const choiceC = document.getElementById("C");
const choiceD = document.getElementById("D");
const counter = document.getElementById("counter");
const timeGauge = document.getElementById("timeGauge");
const progress = document.getElementById("progress");
const scoreDiv = document.getElementById("scoreContainer");
const sorpresa = document.getElementById("sorpresa");
const popUpSorpresa = document.getElementById("popUpSorpresa");

// create our questions
let questions = [
    {
        question : "¿Cual es la verdadera identidad de Mr. Increíble?",
        choiceA : "Robert 'Bob' Parr",
        choiceB : "Bruce Wayne",
        choiceC : "Kal-El",
        choiceD : "Wally West",
        correct : "A"
    },{
        question : "¿A cual super heroe corresponde la imagen?",
        imgSrc : "assets/img/trivia11/wonderwoman.jpg",
        choiceA : "Thor",
        choiceB : "Superman",
        choiceC : "Mujer Maravilla",
        choiceD : "black widow",
        correct : "C"
    },{
        question : "¿A cual super heroe corresponde la canción?",
        audSrc: "assets/audio/spidemar-song1.mp3",
        choiceA : "Capitan America",
        choiceB : "Iron Man",
        choiceC : "Spiderman",
        choiceD : "Shazam",
        correct : "C"
    },{
        question : "¿Carol Danvers es mejor conocida como?",
        tipo:"S",
        premioIns:500,
        choiceA : "Carol",
        choiceB : "Capitana Marvel",
        choiceC : "Danvers",
        choiceD : "Mujer Maravilla",
        correct : "B"
    },{
        question : "¿Black Widow nacio en?",
        choiceA : "Alemania",
        choiceB : "Canada",
        choiceC : "Estados Unidos",
        choiceD : "Union Sovietica",
        correct : "D"
    },{
            question : "¿Red Skull es el archienemigo de ?",
            tipo:"S",
            imgSrc : "assets/img/trivia11/redSkull.png",
            premioIns:1000,
            choiceA : "Superman",
            choiceB : "Capitan America",
            choiceC : "Batman",
            choiceD : "Mujer Maravilla",
            correct : "B"
    },{
            question : "¿La mujer invisible Forma parte de ?",
            choiceA : "los 4 Fantasticos",
            choiceB : "Los Vengadores",
            choiceC : "X-Men",
            choiceD : "Jovenes Titanes",
            correct : "A"
        }



];

// create some variables

const lastQuestion = questions.length - 1;
let runningQuestion = 0;
let count = 0;
const questionTime = 15; // 15s
const questionTimeBonus = 5; // 5s
const gaugeWidth = 150; // 150px
const gaugeUnit = gaugeWidth / questionTime;
let TIMER;
let score = 0;
let puntuacion = 0;
let EsSor="";
let premioSor=0;
let countS=0;
let popS=2;

// render a question
function renderQuestion(){
    let q = questions[runningQuestion];
  
    if(q.tipo==="S" ){
        EsSor="S";
        premioSor=q.premioIns;
        PreSorpresa();
        
    question.innerHTML = "<p>"+ q.question +"</p>";
    if (q.imgSrc!== undefined ){
        qImg.innerHTML = "<img src="+ q.imgSrc +">";
    }
    else{
        qImg.innerHTML ="";
    }

    
    if (q.audSrc !== undefined ){
        qAud.innerHTML ="<audio src="+ q.audSrc +" preload=auto autoplay controls>";
    }
    else{
        qAud.innerHTML="";
    }
    

    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
    choiceD.innerHTML = q.choiceD;
  

    } 
    else{
        sorpresa.classList.remove("card-header-warning");     
        popUpSorpresa.style.display = "none";    

    question.innerHTML = "<p>"+ q.question +"</p>";
    if (q.imgSrc!== undefined ){
        qImg.innerHTML = "<img src="+ q.imgSrc +">";
    }
    else{
        qImg.innerHTML ="";
    }

    
    if (q.audSrc !== undefined ){
        qAud.innerHTML ="<audio src="+ q.audSrc +" preload=auto autoplay controls>";
    }
    else{
        qAud.innerHTML="";
    }
    



    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
    choiceD.innerHTML = q.choiceD;


    }
}

start.addEventListener("click",startQuiz);

// start quiz
function startQuiz(){
    start.style.display = "none";
    quiz.style.display = "block";
    renderQuestion();
    
    quiz.style.display = "block";
    renderProgress();
    renderCounter();
    TIMER = setInterval(renderCounter,1000); // 1000ms = 1s
}

// render progress
function renderProgress(){
    for(let qIndex = 0; qIndex <= lastQuestion; qIndex++){
        progress.innerHTML += "<div  id="+ qIndex +">  </div>";
  
    }
    
}

// counter render

function renderCounter(){
    if(count <= questionTime){
        counter.innerHTML = count;
        timeGauge.style.width = count * gaugeUnit + "px";
        count++
        
    }else{
        count = 0;
        // change progress color to red
        answerIsWrong();
        if(runningQuestion < lastQuestion){
            runningQuestion++;
           
            renderQuestion();
        }else{
            // end the quiz and show the score
            clearInterval(TIMER);
            scoreRender();
        }
    }
}

// checkAnwer

function checkAnswer(answer){
   
    if( answer == questions[runningQuestion].correct){
        // answer is correct
        score++;

        //bonus por responder rapido
        if (count<questionTimeBonus){
            puntuacion+=200;
            if(EsSor==="S"){
                puntuacion+=premioSor;    
            }
        }else{puntuacion+=100;
            if(EsSor==="S"){
                puntuacion+=premioSor;
    
            }
        }
        //premio instantaneo

        
     
        //pun.innerHTML = "<div class='po' " +">"+puntuacion + "</div>";
        pon.innerHTML = puntuacion;
        // change progress color to green
        answerIsCorrect();
    }else{
        if(popUpSorpresa.style.display === "block" ){
            renderCounterSorpresa();
        }
        //pun.innerHTML = "<div class='po' " +">"+puntuacion + "</div>";
        pon.innerHTML = puntuacion;
        // answer is wrong
        // change progress color to red
        answerIsWrong();
    }
    count = 0;
    if(runningQuestion < lastQuestion){
        runningQuestion++;
       
        renderQuestion();
    }else{
        // end the quiz and show the score
        clearInterval(TIMER);
        scoreRender();
    }
}

// answer is correct
function answerIsCorrect(){
    document.getElementById(runningQuestion).style.backgroundColor = "#0f0";
}

// answer is Wrong
function answerIsWrong(){
    document.getElementById(runningQuestion).style.backgroundColor = "#f00";
}

// score render
function scoreRender(){
    scoreDiv.style.display = "block";
    
    scoreDiv.innerHTML += "<p class='col-md-12' >"+"PUNTOS TOTALES "+ puntuacion +"</p>";
   
}

// Pregunta sorpresa render
function PreSorpresa(){

    popUpSorpresa.style.display = "block";
    popUpSorpresa.innerHTML = "<p class='col-md-12' >"+"Esto es una pregunta Sorpresa por "+premioSor +" Puntos "+"</p>";
    sorpresa.className+=" card-header-warning";
  
}

function renderCounterSorpresa(){
        popUpSorpresa.style.display = "none";    
        count=10;    
}


















