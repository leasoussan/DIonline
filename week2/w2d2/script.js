// alert("Daily Challenge Week2 day2 ")

// Daily Challenge : Not Bad
// Create a string that has the word “not” and “bad” inside
// Create another variable that should find the first appearance of the substring “not” and “bad”.
// If the ‘bad’ follows the “not”, then it should replace the whole “not”…”bad” substring with ‘good’ than console.log the result.
// If it doesn’t find “not” and “bad” in the right sequence (or at all), just console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad!', the result is : 'This dinner is good!'
//   Your string is : 'This movie is not so bad!' the result is : 'This movie is good!'
//   Your string is : 'This dinner is bad!' the result is : 'This dinner is bad!'

let sentence = prompt('Tell me something with not and bad in it')
let words = sentence.split(" ")

let not = words.indexOf("not")
let bad = words.indexOf("bad")
// let change = not += bad 
// console.log(change)
let remove = words.splice(not, 2, "good")

console.log(remove)

// let better = words.replace("not bad", "good")


// console.log(better)
// if (change == true){
//     console.log(better)
// }

// console.log("not is located at "+ not + "position, and BAD is located at " +bad+ "position of this sentence")
