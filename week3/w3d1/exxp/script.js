// alert("week3 day1 XP Excercice")
// 
// Exercise 1 : Change The Navbar

// In the div above, change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new li to the ul.
// First, create a new li tag (use the createElement method)
// Then create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstChild and the lastChild properties to retrieve the first and last li elements under the parent ul node. 
// Display the text of each link.(Hint: nodeValue property).


// var changeID = document.getElementById("navBar")
// changeID.setAttribute("id", "socialNetworkNavigation")

// // console.log(changeID)


// var list = document.querySelector("ul")
// var newLi = document.createElement("li")
// var textLi =document.createTextNode("new LI")
// newLi.appendChild(textLi)
// list.appendChild(newLi)

// console.log(newLi)


// var fctio = document.querySelector("ul")
// var logout = document.createElement("li")
// var text = document.createTextNode("Logout")
// logout.appendChild(text)
// fctio.appendChild(logout)
// console.log(logout)

// var ul = document.querySelector("ul")
// var premier = ul.firstElementChild
// var dernier =ul.lastElementChild
// console.log(premier.innerHTML)
// console.log(dernier.innerHTML)







// --------------------EXERCICE 2----------------------------------------------
// Change the name “Pete” by “Richard”
// Change each first name of the <ul> by your name
// Add at the end of each <ul>, a <li> that says “Hey students”
// Delete the <li> Sarah
// Bonus
// Add a class “student_list” to both of the <ul>
// Add the class “university” and “attendance” to the first <ul>



let ul1 = document.querySelector("ul");
console.log(ul1);
ul1.lastElementChild.innerHTML= "richard";

let ul2 = document.querySelectorAll("ul")[1];

ul1.firstElementChild.innerHTML= "leo"
ul2.firstElement.innerHTML= "lea"
console.log(ul2)    



var addText = document.getElementsByTagName("ul");
var hello = document.createElement("li");
var text = document.createTextNode("Hey Students");
addText.appendChild(text)




// ____________--EXCERCICE 3______________________

// Exercise 3 : Change The Logo
// Open up Github in Chrome or Firefox, and open up the console.
// Find the Github navbar and store it in a variable. Use the DOM properties and methods to retrieve the element node. Don’t add an id or a class the the element.
// Change the color of the navbar.
// Find your Github name and store it in a variable.
// Change your name by “The Boss”

// let header = document.querySelector(".Header")
// // undefinedwe seleceted the .Header  as it's a class refereance 
// header.style.backgroundColor= "orange"
// "orange"


// let changeMe = document.querySelectorAll(".user-profile-link")
// changeMe.innerText = "PROFESIONEL"



// ---------------EXCERCICE 4-------------------------------

// For the following exercise use this website for assistance:
// 1. Add a “light blue” background color and some padding to the div above.
// 2. Do not display the first name (John) in the list and add a border to the second name (Pete).
// 3. Change the font size of the whole body.
// 4. Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div)

// var div = document.querySelector("div")
// div.style.backgroundColor = "lightblue"
// div.style.padding = "20px"

// // console.log(blue)

