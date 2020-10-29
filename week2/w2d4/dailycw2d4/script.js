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


function starWords (){
    let getsentence = prompt("What do you like most -seperate by coma");
    let splitw = getsentence.split(',')
    
    let border = "*".repeat(getsentence.length)
    console.log(border)
    for (word of splitw){
        console.log("*" + " " + word + " ".repeat(getsentence.length - word.length -3) + "*") 
        // the -3 are the stars that are att eh stars to allign to the left 

    }
    console.log(border)
}


// ------OTHER SOLUTION-----------------------
// function framedString (phrase) {
//     let arr = phrase.split(", ")
//     let longest = 0;
// ​
//     for (w of arr) {
//         if (w.length > longest) {
//             longest = w.length
//         }
//     }
//     let line = ""
//     let something = ""
//     for (i=0; i<longest+4; i++) {
//         line += "*"
//     }
//     console.log(line)
// ​
//     for (word of arr) {
//         let numMarginR = longest +1 -word.length;
//         rightSpaces = ""
//         for (i=0; i<numMarginR; i++) {
//             rightSpaces += " ";
//         }
//         console.log("* " + word + rightSpaces + "*")
//     }
//     console.log(line)
// }
// ​
// framedString("Hello, how, are, beauiful, you")





starWords()
   
// function starWords (sentence){
//     let words = sentence.split(',').join('\r\n');
//     let longw = 0; 

//    for (let w = 0; w < words.length; w++){
//        if (entry[w].length > longw){
//            longw = entry[w].length 
//        }
//        return longw
//     }

// /console.log(starWords(prompt("What do you like most to do   seperate every word with coma?")))
