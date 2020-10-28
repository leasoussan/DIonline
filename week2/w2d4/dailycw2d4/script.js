// alert("Daily Challenge W2 D4")

// Daily Challenge : Words In The Stars
// Ask a user for several words (separated by commas).
// Push the words into an array.
// Console.log them, one per line, in a rectangular frame.
// For example, if the user gives you:
// Hello, World, in, a frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

// stars and words
// Hint:

// The number of stars that wraps the sentence, must depend on the length of the longest word.
// Requirements:

// To do this challenge you only need Javascript(No HTML and no CSS)

let entry = prompt("What do you like most to do   seperate every word with coma?");
   
function starWords (sentence){
    let words = entry.split(',').join('\r\n');
    let longw = 0; 

   for (let w = 0; w < words.length; w++){
       if (entry[w].length > longw){
           longw = entry[w].length 
       }
       return longw
    }
}
console.log(starWords(entry))
