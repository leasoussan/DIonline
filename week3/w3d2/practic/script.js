// alert("Week 3 day2 practice")

// Event Listener are fuction to give to element that you select first to be done when cliked
// var button = document.getElementById("xxx")`` 
// function alerUser(){
//      prompt/alert etccc
//  }
//  button.addEventListener('clikc', alertUser)
// or GamepadButton.removeEventListener('click', function)

// the function can be inside 
// button.eventListener("dbclikc", finction(){
//     write the function here if you dont need a function that u reuse again 
//     otherwise better to be outside as a global function
// }


//  mousover- another event listener
// LOOK JS event List 

// FOCUS and BLUR tochange the focus of the elements

// ** Enable function**
//Load event- to load the javascript beofre (check usage)

// this.className = 'text red'
// this is to call CSS element no need.



// Modifying event you can style stuff with DOM event

//  EX1 -DOM EVENT NOTE
// Write a JavaScript function to add rows to a table. Use the code below as a base
// function insert_Row(){
//     let table =document.getElementById("sampleTable");
//     let row = document.createElement("tr");
//     row.innerHTML = "<td>Cell </td><td>Cell </td>"
//     table.appendChild(row);
// }

let btn = document.getElementById("jsstyle");
btn.addEventListener("click", function(){
    btn.style.backgroundColor = "green";
    btn.style.fontSize = "4em";
    
})


btn.addEventListener('click', pushbtn);

function pushbtn(){

    btn.innerHTML='Magic!';
    let div = document.createElement("div");
    div.style.backgroundImage="url(https://res.cloudinary.com/practicaldev/image/fetch/s--D-aJRe8W--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/d7oeukl09h4vemh75dl0.png)";
    div.style.width ="400px";
    div.style.height= "400px";
    div.style.backgroundSize= "cover";
    document.body.insertBefore(div, btn);
    
}

document.addEventListener('keypress', hello);


function hello(){

    let cercle = document.createElement('div');
cercle.style.backgroundColor="red";
cercle.style.borderRadius="50%";
cercle.style.width ="100px";
cercle.style.height= "100px";
cercle.style.textAlign ="center";
cercle.style.margin ="auto";
circle.innerHTML= "DANGER ZONE!";
circle.style.color ="white";
document.body.insertBefore(cercle, btn)
}
// document.onkeydown =function(evt){}
