// alert("Ex XP week3 day 2")


// EX1
// Give to all paragraphs inside the <article> tag the class of para_article.
// Remove the last paragraph in the article.
// Add an event listener so that when you click on the h2, it is removed from the DOM.
// Set the font size of the h1 to be a random pixel size from 0 to 100.
// Hide the 1st paragraph, when it’s clicked. (use the display property )
// Get the values from the inputs and append them to the end of the html, inside a table.
// Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.


// let para = document.getElementsByTagName("p");
// let article = document.querySelectorAll("article")[0];

// for (i =0; i < para.length; i++){
//     para[i].className="para-article";
// }

// let lastp = document.querySelector("article").lastElementChild;
// // console.log(lastp)

// lastp.remove()






// // REMOVE H2
// let text = document.querySelector("h2");
// text.addEventListener("click", deleath2)

// function deleath2(){
//  text.remove();
// }

// // random h1
// let h1 = document.querySelector('h1');
// console.log(h1)
// h1.style.fontSize = Math.floor(Math.random() * 100) +"px";

// // Hide 1st prargrapg
// let hidep = document.querySelector("para"[0]);
// hidep.addEventListener("click", removep)

// function removep(){
//     hidep.style.display="none";
// }

// // INPUT Collection

// let newInput1 = document.getElementsByTagName('label')[0]

//         newInput1.onchange = function () {
//             firstName.innerHTML = this.value;
//         };




// ex2
// Exercise 2 : Transform The Sentence
// Add this sentence to your html then follow the steps :
// Create a function called : getBold_items() that takes no parameter. This function has to collect all the bold items inside the paragraph.
// Create a function called : highlight() that changes the color of each bold item to blue.
// Create a function called : return_normal() that changes the color of each bold item to black.
// Call the function highlight() onMouseOver and the function return_normal() onMouseOut





// Excercie 3
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:


// function calculate(){

// let radius = document.getElementById("radius").value
// console.log(radius)

// let volume = document.getElementById("volum")
    
// }

let radius = document.getElementById("radius").value;
console.log(radius)

// Excercice 4