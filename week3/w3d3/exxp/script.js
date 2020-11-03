// Exercise 1 : Move The Box
// Move the box from left to right
// Tip: use setInterval
// 
//first I want to ceck the button properties -onclick="myMove"-done
//2nd I want to creat a function myMove (gave this name to my bytton onclick)

//1) ineed to get the element I want to manipulate 

// let yellow = document.getElementById("container")
// let red = document.getElementById("animate")
// //possible to give some mor attribute 
// yellow.classList.add("outer")
// red.classList.add("inner")
// yellow.append(red)


// function myMove(){
//     var redMove = document.getElementById("animate");
//     var position = 0;
//     //here I would like first to add the function set interval for the square to move 
//     //this would be according to the size of the yellow box width 400px- because the red is 50px the max it can go is 350
//     let move = setInterval( function(){
//         if (position == 350){
//             clearInterval(move)
//         }
//         else{
//             redMove.style.top = position + "px";
//             redMove.style.right = position + "px";
//         }
//     }, 5)
// }




//for info
//set interval function 
// myVar = setInterval("javascript function", milliseconds);

//clearInterval function
// clearInterval(myVar);



// ---------------------EX2______________________

// Exercise 2: Drag & Drop
// Create a draggable square/box element.
// Drop it in a specific box.
//firt in the HTML if have created a big div with 2 div inside element1 and 2
// i have to set whom they will be the draged or the droped 
// what ever I want to be gragable have to have draggable="true"
//the ones moving will be ondragstart="drag(event)"
//now I have to define the events -functions 




function allowDrop(event) {
    event.preventDefault();
}



function drop(event) {
ev.preventDefault();
var data = ev.dataTransfer.getData("text");
ev.target.appendChild(document.getElementById(data));
}

function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    event.target.appendChild(document.getElementById(data));
  }


  -----------------------------ex web site-----------------

  // HTML AND JS


function allowDrop(event) {
    event.preventDefault(); // Necessary. Allows us to drop.
  }
  
  //add dashes
  function allowEnter(event) {
    event.target.classList.add('over');
  }
  
  //remove dashes
  function allowLeave(event) {
    event.target.classList.remove('over');
  }
  
  function dragStart(event) {
  //set the data to be dragged
  console.log("target:",  event.target)
  console.log("id: ",  event.target.id ) // id: square1
  event.dataTransfer.setData("text", event.target.id);
  }
  
  function dragDrop(event) {
  // console.log("event.target:",event.target) 
  // "event.target:" "<div id='square3' ondrop='dragDrop(event)' ondragover='allowDrop(event)'>square3</div>"
  event.preventDefault();
  // retrieve the data dragged
    
    
  let data = event.dataTransfer.getData("text");
  console.log("data: ",  data) //data: square1 
    
  let box = document.getElementById(data)
  event.target.appendChild(box);
  }
  
  // Only JS
  
  let square1 = document.getElementById("square1")
  let square3 = document.getElementById("square3")
  
  square1.addEventListener("dragstart", dragStart)
  
  function dragStart(event){
    event.dataTransfer.setData("text", event.target.id);
  }
  
  ///END OF SQUARE 1////
  
  ///BEGINNING OF SQUARE 1///
  square3.addEventListener("dragover", dragOver)
  square3.addEventListener("drop", drop)
  square3.addEventListener("dragenter", dragEnter)
  square3.addEventListener("dragleave", dragLeave)
  
  //1st step of drop target
  function dragOver(event){
    event.preventDefault();
  }
  
  function drop(event) {
    event.preventDefault();
    let dataSquare = event.dataTransfer.getData("text");
    let box = document.getElementById(dataSquare)
    event.target.appendChild(box);
  }
  
  function dragEnter(event){
    // event.target.style.backgroundColor = "green"
     event.target.classList.add('over');
  }
  
  function dragLeave(event){
    // event.target.style.backgroundColor = "lightblue"
    event.target.classList.remove('over');
  }
  