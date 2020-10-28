// alert('XP GOLD EX Week2 Day4')

// Exercise 1 : Tips
// John and his family went on a holiday and went to 3 different restaurants.
// To tip the waiter a fair amount, John created a simple tip calculator (as a function).

// He likes to tip:
// 20% of the bill when the bill is less than $50,
// 15% when the bill is between $50 and $200,
// and 10% if the bill is more than $200.

// Ask John for the amount of the 3 bills. He has to enter a list of bills, each one separated by a comma.
// Create the program explained above.
// In the end, John would like to have 2 arrays:
// Containing all three tips (one for each bill).
// Containing all three final paid amounts (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)


// let resto = toPay.split('')

function tipCalc(topay){
    if (topay < 50){
        return topay*0.2
    }
    else if (topay >=50 && topay < 200){
        return topay*0.15
    }
    else if (topay >= 200 ){
        return topay*0.1
    }
    }

console.log(tipCalc(prompt("how much did you pay")))


function expenses(dinner){
    for (dinner > 0 ) {
        
        return dinner.split(",")
    }
}
    console.log(prompt("how much did you spend -divid with coma"))








// Exercise 2 : Play A Guessing Game
// Create tow files : index.html and style.css
// Go to this github link and copy the content into your files.
// Then, follow the steps written below
// Steps
// Explanation of the game : the point of the game is to guess the number that the computer has in “mind”.

// First Part
// Create a JS file and link it to the index.html file.
// Look at the and of your html file, you should have a button with an “onclick” event. This event is equal to the function playTheGame(). It means that when you will click on the button, the function playTheGame() will be called.
// We will learn more on events next week ;)
// Now let’s create the function:
// In the JS file, create a function called playTheGame() that takes no parameter.
// In the function, start by asking the user if he wants to play the game (Hint: use the built-in confirm() function)
// If his answer is negative alert him “No problem, Goodbye”
// If his answer is positive, then do the following steps:
// Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :
// If he didn’t enter a number (ie. if he entered another data type) alert him “Sorry Not a number, Goodbye”.
// If he didn’t enter a number between 0 and 10 alert him “Sorry it’s not a good number, Goodbye”.
// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber. Assign to this variable a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.
// Second Part
// Outside of the playTheGame() function, create a new function named test(userNumber,computerNumber) that takes 2 parameters : userNumber and computerNumber
// The point of this function is to check if the userNumber is the same as the computerNumber:
// If userNumber is equal to computerNumber, alert the user that he won and stop the game.
// If userNumber is bigger than computerNumber, alert the user that it’s bigger and that he has to guess again. (Hint: use the built-in prompt() function to ask the user for a new number)
// If userNumber is lower than computerNumber, alert the user that it’s lower and that he has to guess again.
// If the user guessed more than 3 times, alert him that he can’t try again and display the number that the computer had in mind.
// Third Part
// You have to call the test(userNumber,computerNumber) function somewhere. Find where you have to invoke it, and then invoke it.
// Bonus
// In the First Part, instead of stopping the process if the user didn’t enter a valid number. Continue asking him for a number until he enters a valid one.
