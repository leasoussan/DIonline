// create a stuctured html file linked to a JS file

// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"

// for (let i = 0; i < 15; i++) {
//     if (i % 2 == 0){
//     console.log(i+ "is Even")
//     }  else  
//     console.log(i+ "is Odd")
// }

// let friends = ["david", "sarah", "paul", "lea"];

// for (let i = 0; i < friends.length; i++){
//     console.log("hello" +friends[i])
// }

// _________________________CLASS NOTE___________________
// let colors = ["blue", "yellow", "red"];

// for (let item of colors) {
//    console.log("the color is ", item);
// }


// let shoppingList = {
//     fruit: "pear",
//     meat : "chicken",
//     drink : "cola"
// }

// for (let shoppingitem in shoppingList) {
//    console.log("I have to buy ", shoppingList[shoppingitem]);
// }


// for (let i = 0; i < 10; i++) {
//     if (i === 3) { 
//         continue;
//       }
//     console.log("The number is " + i);
// }

// let age = 12

// if (age === "12"){
//     console.log("true")
// } else {
//     console.log("false")
// }
// _____________________________________________________________






// Exercise 3
// var names= ["john", "sarah", 23, "Rudolf",34]

// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.

// var names= ["john", "sarah", 23, "Rudolf",34]


// name = name.charAt(0).toUpperCase() + name.slice(1) 


// for (let i = 0 ; i > names.lenght; i++){
//     if(isNAN names[i]  === true ) {
//         if(names[i].chartAt(0).toUpperCase()==true){}
//         console.log(names[i]);
//     }
// }



// let names = ["john", "sarah", 23, "Rudolf", 34];
// for (let i=0; i < names.length; i++){
//     if(isNaN(names[i])){
//         if(names[i].charAt(0) == names[i].charAt(0).toUpperCase()){
//             console.log("name in uppercase:", names[i]);
//         } else{
//             console.log("name not in uppercase:", names[i]);
//             names[i]= names[i].charAt(0).toUpperCase() + names[i].slice(1)
//             console.log("name now in uppercase:", names[i]);
//         };
//     }
//     else {
//         console.log("not a string", names[i])
//         continue;
//     }
// }