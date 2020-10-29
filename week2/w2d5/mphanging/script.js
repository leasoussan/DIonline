// Create A Hanging Game:
// Create the “Hangman” game. Your game will run in the console only.
// You need to guess a hidden word. Each letter you guess will appear, and you have 10 wrong guesses before you lose the game.
// Check it out here

// Player 1 enters a word. The secret word has to have at least 8 letters. It must be displayed as stars in the console.
// Eg. Player 1 chooses the word “javascript”.
// The word is displayed in the console as “**********“
// Player 2 guesses a letter.
// Eg. “s”. The console must now display “****s*****“
// If the player guesses “a”, BOTH corresponding letters must be displayed, like this: “*a*as*****".
// Some Extra Rules:
// -The user will have 10 “lives” with which to guess the word. If they guess an incorrect letter, they lose a life.
// -You should also display a list of the incorrect letters chosen.
// -You should prevent a user from rechoosing an already chosen letter (correct or incorrect).
// -A message should inform the user when they win or lose.

// My Logic to the game:
// 1) I would  like to set a word that the player would have to guess
// 2) I want the player to enter letters to guess up to 10 
// 3) I want to check if the letters i enter are matching the letters 
// 4) if they exist _ i want the to be pushed into a displayed array 
// 5) if they dont exist I would like to have a results 


// Get a secret word
let secret  = ["absolute","abstract","academic","accepted", "accident","accuracy", "accurate", "achieved"]
let secretWord = secret[Math.floor(Math.random()*secret.length)].slice("");

// get word in *
var answerArray = [];
for(i =0 ; i< secretWord.length; i++){
    answerArray[i] = "*";
}
// console.log(answerArray)

// get reminding letters we get by knowing how many letters there is in the word 
var wordletters = secretWord.length
numGuess = 10

while ( numGuess < 10){
    let guess = prompt("guess a letter");
    if (guess.length !==1){
        alert("please enter one letter")
    }else {
        for (var j =0; j < secretWord.length; i++){
            if (secretWord[j] === guess){
                answerArray[j]=guess}
                wordletters--;
            }
        }
    }


// function getWord (start){
// let getInput = prompt("Enter the word to be guessed");
// getInput = getInput.toLowerCase.split("");
// var wordstar = [];
// var guess = 10;
// var guessLetter = []

// for (i =0; i< guess; i++){
//     if 

// function guessWord(letters)
//     let word = getWord();
//     let nbrGess = 10; 
//     let guess = prompt("enter a letter")
//     let wordCheck = guess 

    
//     
//     }
    
//     }


