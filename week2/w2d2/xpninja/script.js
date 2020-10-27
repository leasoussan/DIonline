// alert(" XP NINJA Week2 day2 ")

// Exercise 1 : Age Difference
// Given the birthdates of two people, find the date when the younger one is exactly half the age of the other.
// Notes: The dates are given in the format YYYY

// let pers1 = prompt("whats you birthday date?")
// let pers2 = prompt("whats is you birthday person number2?")


// dob1 = 2020 - pers1
// console.log("pers1 is " + dob1 +"years old")

// dob2 = 2020 - pers2
// console.log("pers2 is " + dob2 +"years old")
 

// if (dob1 < dob2){
//     console.log("in"+ ((dob2%dob1)+2020)  + "you will be half his age")
// }else console.log("in" +((dob1/2)-dob2+2020 ) +" you will be half his age")
// else console.log("in"+ ((dob1%dob2)+2020)  + "you will be half his age")
// )


// Exercise 2 : Zip Codes
// Harder exercise
// Hint : Use Regular Expression
// You are working in a PostOffice and you need the zip code of the clients in order to send them letters.
// Ask your client for his zip code and console.log “good” or “error” based on the following rules.
// A valid zip code is as follows:
// Zip codes consist of 5 consecutive digits
// Must only contain numbers (no non-digits allowed).
// Must not contain any spaces.
// Must not be greater than 5 digits in length.

// let zip= prompt("Whats your zip code")

// if (zip.length(!= 5){
//  console.log("error")
// } else
// console.log("good")

// (zip.includes( !=Number)
// && )) || (zip.includes(" ")))

// Exercise 3 : Secret Word
// Harder exercise
// Hint : Use Regular Expression

// Ask the user for a word and save it in a variable.
// Delete all the vowels of the string and console.log the result
// Bonus: Replace the vowels with another character and console.log the result
// a = 1
// e = 2
// i = 3
// o = 4
// u = 5

let word = prompt("give me a word")
let voyel =["a","e","i" ,"o" ,"u"]

let letter = word.split();

let check = letter.filter(voyel)

console.log(check)

// if (letter.includes()){
//     letters =str.replace("a"=1, "e"=2, "i"=3, "o"=4, "u"=5);
//     console.log(letter)
// }
