// alert("Calculator mini project")


// You see in the html file below some “onclick” events. It means that, when you will click on the button, the function my_f(argument)
// will be called with a specific argument.
// For example, if you click on the number 2, the function my_f(2) will be called. The argument is the value of the button.
// (Don’t worry, we will learn events next week)
// You have to create the function my_f(argument) in the JS file, and write your program inside.
// You can create several different functions in order to split your code into smaller parts (easier to understand).
// Before coding, take your time to understand all the parts of the exercise, and the process. You can right it sown somewhere if it helps (recommended)
// ONLY when you are done, you can improve the style of the calculator.
// Bonus : create the RESET and CLEAR buttons.

let calcDisplay = document.getElementById("display")

console.log(calcDisplay)

let calcstr = ""




function my_f(btn){
    calcstr = calcstr + btn;
    calcDisplay.innerHTML = calcstr;
    // console.log(calcDisplay)
}

function result(){
    let calcresult= eval(calcstr);
    calcDisplay.innerHTML = calcresult;
}

function c(){
    calcstr = "";
    calcDisplay.innerHTML = 0;
}

function remove(){
    if (calcDisplay.innerHTML.length>0){
        calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0, -1)
    }
}
