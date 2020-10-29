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

let zip= prompt("Whats your zip code")

if (zip.length(!= 5){
 console.log("error")
} else
console.log("good")

(zip.includes( !=Number)
&& )) || (zip.includes(" ")))

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


        //About Regex:

        // A regular expression is an object that describes a pattern of characters.
        // Regular expressions are used to perform pattern - matching and "search-and-replace" functions on text.

        //https://www.youtube.com/watch?v=sXQxhojSdZM
        //https://www.w3schools.com/jsref/jsref_obj_regexp.asp
        //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Assertions
        //Character classes: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Character_Classes
        // Test Your Regex: https://regex101.com/
        //Learn More: https://www.youtube.com/watch?v=909NfO1St0A



        //http://learn.di-learning.com/courses/collection/3/course/10/section/34/chapter/115#

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


        // Solutions:



        //Without Regex:

        // var zip = prompt("what is your zipcode ?");

        // if (zip.length !== 5 || isNaN(zip)) {
        //     console.log("ERROR")
        // } else {
        //     console.log("Very Good")
        // }



        //With Regex:

        // let zipPrompt = prompt("Write your code here");
        // pattern = /^\d{5}$/;
        // console.log(pattern.test(zipPrompt))


        //Use ^ to fix the matching at the begining of the string, and right after newline.
        //Use $ to fix matching at the end of the text.

        //The regex matching 5 consecutive digits is:  \d{5}
        //The regex only numbers: \d 
        //Must not contain any spaces: \S
        //Must not be greater than 5 digits: \b\d{5}\b



        //https://stackoverflow.com/questions/50813606/how-to-disallow-consecutive-five-digits-and-more-using-regex
        //https://stackoverflow.com/questions/9011524/regex-to-check-whether-a-string-contains-only-numbers
        //https://stackoverflow.com/questions/22082054/regex-to-match-if-no-space-is-found
        //https://www.regextester.com/110149







        // Exercise 3 : Secret Word
        // Harder exercise
        // Hint: Use Regular Expression

        // Ask the user for a word and save it in a variable.
        // Delete all the vowels of the string and console.log the result
        // Bonus: Replace the vowels with another character and console.log the result
        // a = 1
        // e = 2
        // i = 3
        // o = 4
        // u = 5


        //Solution:

        // Search for Regex solution: js regex delete all vowels
        //https://stackoverflow.com/questions/53144030/how-do-i-remove-all-vowels-from-a-string-and-return-the-result-using-a-for-loop/53144045


        // let word = prompt("Enter a word");
        // let word2 = word;
        // word = word.replace(/[aeiouAEIOU]/gi, "");
        // console.log(word);


        // // // BONUS 
        // word2 = word2.replace(/[aeiouAEIOU]/gi, "X");
        // console.log(word2);


        //You need the g flag, and with the i flag you can save the repetition of vowels
        //http://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm


        

        //Regex Test To Match an Email:

        // var regex = /^.+@.+\..+$/;

        // console.log(regex.test('johndoe@gmail.com'));

