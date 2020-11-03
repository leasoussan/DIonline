var css =document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
let body = document.getElementById("gradient");



console.log(body)
console.log(css)
console.log(color1)
console.log(color2)

//to chosea new color


//in order to dot he change we will write this twice one for each color but as we dont have to repeat we will write it as bellow
// color1.addEventListener("input", function(){
//    body.style.background =  "linear-gradient(to right," +color1.value + "," + color2.value + ")";
// })

function setGradient(){
    body.style.background = 
     "linear-gradient(to right," +color1.value + "," + color2.value + ")";
    css.textContent = body.style.background +";";
}


//this is JS manipulation - HTML will be without oninput
color1.addEventListener("input", setGradient)

color2.addEventListener("input", setGradient)
    


//in order to change the background color according to the colors 
//we get the body in order to change the background

//now we would like to change the background with the color we chose
//we can change like this 
// body.style.background ="red"


//we could on the html in the input add oninput=setGradient()  as we have the function and the css it would of been executed
//see html