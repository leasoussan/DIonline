// alert("Daily Challenge week3 day 2")


// Daily Challenge : Tell The Story
// This webpage has the start of a Mad Libs game.
// If you’ve never played it, that’s a game where you fill in a 
// bunch of blanks inputs with different word types 
// (ie : noun, adjective, verb), and then a story is generated based on those words, 
// and sometimes the story is surprisingly funny.
// In this step, you’re going to finish the game logic 
// in the event listener (check out the script tag below).

// Follow these steps :

// find the value of each of the input
// write out a story that uses each of the values
// Make sure you check the console for errors when you play the game.






let libButton = document.getElementById('lib-button');

let libIt = function() {
let storyDiv = document.getElementById("story");
let noun1 = document.getElementById("noun").value;
let adjectiv = document.getElementById("adjective").value;
let person = document.getElementById("person").value;
storyDiv.textContent = " its been a very long day, where"+ person + "came to visite me in the city. This day I had" + noun1 + "i wanted to play a bit  so we gathered our toughts and we " + adjectiv + " at the end I decided to go home";

};

libButton.addEventListener('click', libIt);
    
