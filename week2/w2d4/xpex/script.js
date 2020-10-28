// Exercise 1 : Keyless Car
// Make a keyless car EVEN BETTER!
// This is the code of the previous part of the exercise :

// let age = prompt("What is your age?");

// if (Number(age) < 18) {
//     alert("Sorry, you are too yound to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// Create a function called checkDriverAge() that will contain the code above. Call the function and notice the benefit in having a function instead of a simple if/else if/else statement.
// Instead of using prompt, make the checkDriverAge() function accept an argument : age, so that if you enter:
// checkDriverAge(92); it console.log “Powering On. Enjoy the ride!”
// 


// function checkDriverAge(age){  
//     if (age <= 18) {
//         return "Sorry, you are too yound to drive this car. Powering off";
//         } else if (age > 18) {
//         return "Powering On. Enjoy the ride!";
//         } else if (age === 18) {
//         return "Congratulations on your first year of driving. Enjoy the ride!";
//         }
//     }
//     console.log(checkDriverAge(prompt("whats your age??")))





// Exercise 2 : Is_Blank
// Write a program to check whether a string is blank or not.

// console.log(is_Blank('')); --> true
// console.log(is_Blank('abc')); --> false

// function is_blank (string){
//     if (string.length == 0){
//     return true;
//     }else{
//     return false
//     }
//     }
//     console.log(is_blank("Eat " ))
 
    
// function pushToList (list){
//     if (is_blank(list)== true){
//         list.push(prompt("Stuff to do"))
//     }
//     else {
//         console.log(list)
//     }
// }

//     console.log(pushToList("Sleep"))







// Exercise 3 : Abbrev_name
// Write a JavaScript function to convert a string in abbreviated form.

// console.log(abbrev_name("Robin Singh")); --> "Robin S."

// function toAbrev(fname, lname){
//         fname = fname
//         lname= lname.slice(0).charAt(0).toUpperCase()
//     return fname + " " + lname
// }

// console.log(toAbrev("lea", "soussan"))






// Exercise 4 : SwapCase
// Write a JavaScript function which accept a string as input and swap the case of each character.
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.


// let entry = prompt("tell me something about ...")

// function caseChange (sentence){
//     let sentenceSplit = entry.split(" ")
//     // console.log(sentenceSplit)
//         for (word of sentenceSplit){
//             let firstletter = word.charAt(0)
//             // console.log(firstletter)
//             let halfWord= word.split(firstletter)
//             // console.log(halfWord)
//                 if (firstletter === firstletter.toUpperCase){
//                     return firstletter.toLowerCase + halfWord.toUpperCase
//                 }
//                 else{
//                     return firstletter.toUpperCase + halfWord.toLowerCase
//                 }
//             }
//             }
// console.log(caseChange(entry))



// Exercise 5 : Amazon Shopping
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }
// Create a function called checkBasket().
// It should:
// ask the user for the item he wants
// and let him know if it’s in the basket or not
// Hint: Use the in keyword inside the conditional
// 






// Exercise 6 : What’s In My Wallet ?
// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.5
// Pennies = 0.1
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// Examples

// changeEnough([2, 100, 0, 0], 14.11) ➞ false
// changeEnough([0, 0, 20, 5], 0.75) ➞ true
// Exercise 7 : Shopping List
// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// Create an array called shoppingList with the values “banana”, “orange”, and “apple”.
// Copy these two above objects into your js file
// Create a function called myBill() that takes no argument.
// Depending on the list of items that you have in your array shoppingList and the prices listed in the prices object,
// return the price spent on shopping.
// Call the function myBill()
// Bonus: In the function above, only add the price if the item is in stock (use the stock object).
// If the item is in stock, decrease the item’s stock by 1
// Exercise 8 : Find The Multiples Of 23
// Write a program that console.log the multiples of 23 less than 500 and at the end return the sum of all of them.

// Elements : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313
// Exercise 9 : Omnipresent Value
// Create a function that determines whether an input value is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.
// To illustrate:

// [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // 3 exists in every element inside this array, so is omnipresent.
// Examples

// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
// Exercise 10 : Vacations Costs
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotel_cost().
// It should ask the user for the number of nights he wants to stay in the hotel.
// If the user’s answer isn’t relevant to the question (ie: if he doesn’t answer, or if the answer is a string), ask him again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
// Define a function called plane_ride_cost().
// It should ask the user for his destination.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
// If the user’s answer isn’t relevant to the question (ie: if he doesn’t answer, or if the answer is a number), ask him again.
// Define a function called rental_car_cost().
// It should ask the user for the number of days he wants to rent the car.
// If the user’s answer isn’t relevant to the question (ie: if he doesn’t answer, or if the answer is a string), ask him again.
// Calculate the cost of renting the car: the car costs $40 everyday.
// If the user rents a car for more than 10 days, he gets 5% discount.
// The function should return the total price of the car.
// Define a function called total_vacation_cost() that returns the total cost of the user’s vacation depending on the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotel_cost(), plane_ride_cost() and rental_car_cost() inside the function total_vacation_cost.
// Call the function total_vacation_cost()
// Bonus: Instead of using a prompt inside the 3 first functions, use a prompt only inside the total_vacation_cost() function. What should you implement for it to work?
