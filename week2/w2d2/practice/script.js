// Exercise 1
// Make a keyless car!

// This car will only let you drive if you are over 18. Make it do the following:

// Using prompt() and alert(), ask a user for their age.

// IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
// IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
// IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"
// age = prompt('How old are you?')

// if (age < 18 ){
//     alert("You are too  too young to drive sorry - go to see you fatha");
// }else if (age == 18){
//     alert("Congratulation you can drive today");
// }else{
//    alert("Power On, Enjoy your ride") 
// }



// Exercise 2
// Write as comments the steps of the resolution of this piece of code

// Guess what will be the result before checking it





// let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }



// Exercise 3
// Write as comments the steps of the resolution of this piece of code

// Guess what will be the result before checking it



// let a = 2 + 7;

// switch (a) {
//   case 4:
//     alert('Right!');
//     break;

//   case 3: // (*) grouped two cases
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
// }



// ----------------OBJECT___________


// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// 2. Create an array which contains the object you have made above and name the array "database".

// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".


let person = {
    username: "lea",
    password: "helloyou",
}

console.log(person)

var database = [person]
console.log(database)

let newsfeed = [];

let pers1 ={
    username: "sarah",
    timeline: "sowhat",
}
let pers2 = {
    username: "jhon",
    password: "surfing",
}
let pers3 = {
    username: "alex",
    password: "eating",
};

newsfeed.push(pers1)
newsfeed.push(pers2,pers3)
console.log(newsfeed)


// or we can do another way to add element into an array 

