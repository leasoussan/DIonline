// alert("this is week2 day3 XP EX")


// / Exercise 1 : Your Favorite Colors
// Create an array to hold your top colors.
// For each choice, console.log a string like: “My #1 choice is blue”
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.
// Hint : create an array of suffix to do the Bonus

// let colors = ["red", "green", "blue", "black", "turqoise"]
// let prefer = ["1st", "2nd", "3rd", "4th", "5th"]

// for (i = 0; i < colors.length; i++){
//     console.log(colors[i]+ " is my " + prefer[i]+ " prefered color ");
// }





// Exercise 2 : Secret Group
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their firstnames, sorted in alphabetical order.
// Console.log the name of their secret society.

// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]

// for (i=0 ; i < names.length; i++){
//     word =console.log(names[i].charAt(0))
// }  

// Correction question: How to put .join()



//------------------------------------
//  Exercise 3 : Repeat The Question
// Ask a number to the user, while the number is smaller than 10, ask him for a new number.
// Tip : Which while loop is more relevant for this situation?
// 


// let n = prompt("give me a number from 0 to 10")


// do {
//     n = prompt("give me a number from 0 to 10");
//     n++;
// } while (n <= 10);



// Exercise 4 : List Of People
// Using a loop, iterate through this array and console.log all of the people.
// Write the command to remove “Greg” from the array.
// Write the command to replace “James” by “Jason” in the array.
// Write the command to add your name to the end of the array.
// 
// let people = ["Greg", "Mary", "Devon", "James"]
// // Itereate name list

// for (i = 0; i < people.length; i++){
//     console.log(people[i]);
// }

// // remove first guy 
// let list1= people.shift(0)
// console.log(people)

// // Change James with Jason
// let change = people.indexOf("james")
// let list2 = people.splice(change, 1, "Jason")
// console.log(people)

// // add my name is first place
// let add = people.push("Lea")
// console.log(people)

// // Using a loop, iterate through this array and after console.log-ing “Mary”, exit from the loop.

// for (i = 0; i < people.length; i++) { 
//     if (people[i] == "Mary");
//     console.log(people[i]);
//     { break; };
//   }



// // Write the command to make a copy of the array using slice. The copy should NOT include “Mary” or your name.

// let list3 = people.slice(1,3)
// console.log(list3)



// // Write the command that gives the indexOf where “Mary” is located.Look on google what indexOfis

// let mary= people.indexOf("Mary")
// console.log(mary)

// indexOf("Mary").chartAt(0).toLowerCase--------TO TRY TO IMPLEMENT THIS !!!!

// // Write the command that gives the indexOf where “Foo” is located (this should return -1).
// let foo= people.indexOf("Foo")
// console.log(foo)



// Write a variable called last which value is the last element of the array.

// let last2 = people[people.length-1]
// console.log(last2)
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
// 







// Exercise 5 : Divisible By Three
// An elementary school’s trick to determine whether or not a number was divisible by three is to add all of the integers in the number together and to divide the resulting sum by three.
// If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.

// Given a series of numbers as a string, determine if the number represented by the string is divisible by three.
// You can expect all test case arguments to be strings representing values greater than 0.
// Example:
// "123"      -> true
// "8409"     -> true
// "100853"   -> false
// "33333333" -> true
// "7"        -> false

// let divid = prompt("lets check if this number can be devided by 3 or not")

// if (divid %3 == 0){
//     console.log("true")
// }else
// console.log("False")




// Exercise 6 : Playing With Numbers
// let age = [20,5,12,43,98,55];
// Requirements : don’t use Javascript methods to answer these questions
// 1. Console.log the sum of all the elements of the array.
// 2. Console.log the largest number of the array.

// let age = [20,5,12,43,98,55];
// let total =" ";

// for (i = 0 ; i < age.length;i++){
//     total += age[i];
//     console.log(total)
// }

// QUESTION 6 CHECK ANSWER 