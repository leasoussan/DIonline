// alert("week3 day3 ")

//function setTimeout function to actin after a time

//there are two arguments(a,b)
// a function is calling another function in the ex is calling to the function sayHi

// function sayHi(phrase, who) {
//     alert( phrase + ', ' + who );
//   }
  
//   setTimeout(sayHi, 1000, "Hello", "John"); //  calls sayHi() after one second --> Hello, John
// // if we would like to add argument to the function you add after the time an argument 


// function sayHi(username) {
//     alert( username);
//   }
//   let nameUser = document.getElementById("inputUserName").value;
//   setTimeout(sayHi, 10000, nameUser);


//``backtick are used make faster 
// function sayHello()
//     alert(`Hello ${username}, you are ${age} year old `)

//sayHello()

// let time = endSale();

let div = document.createElement("div");
let banner = document.createElement("h1");
let clock =10 
// clock doit etre ici pour etre global -elle est accede partous-

function saleBanner(){

    banner.innerHTML= `Sale will end up in ${clock} min`;
    div.appendChild(banner)
    document.body.appendChild(div)
}

setTimeout(saleBanner, 0000,)

// Ex-2


let timer = setInterval(endSale, 1000);


function endSale(){
   
    console.log(clock);
    clock --;
        if (clock < 0){
        clearInterval(timer);
        }
        else {
            saleBanner();
        }
    };



// function endSale(){  
//     if (clock < 0){
//     clearInter();
// }
// }

// function clearInter(){
//   clearInterval(timing);
// }







// to get a repetition of an action
//you have to use a clear interval to help to stop the repetition as otherwise it will go for ever 
  
// example Course note
// let timer = setInterval(myTimer, 1000);

// function myTimer() {
//   let date = new Date();
//   let time = date.toLocaleTimeString();
//   // date.toLocaleTimeString() returns a string with a language sensitive representation of the time portion of this date
//   document.getElementById("demo").innerHTML = time;
// }

// function myStopFunction() {
//   clearInterval(timer);
// }







//Dragging and Drooping 
//according on coordinate (x,y)
//1. get -select the element we want to drag
// 2. set it to draggable element.setAttribut("dragablle", "true")
// we use 2 dif.type of events : dragsStar, dragsEnd event to handle this 

//first event is ("dragstart", function(event))
// taget property = tell us which object was moved (id)
// clientx (horizontal)and client y(vertical) = location of the element to be used to droped element
// event.target.style.backgroundcolor = "newcolor"

// the logic is = you consol log the coordinates from before movment is happenening 