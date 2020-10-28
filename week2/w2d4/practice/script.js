// Exercise 1
// 1. Create a structured html file linked to a js file

// 2. Write a JS function that takes a parameter: myAge

// 3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)

// 4. Call the function

// let myage = prompt("What is your age");

// function askAge (myage){
//     let mum = (myage*2);
//     let dad= (mum*1.2)
//     console.log(myage, "dad's age is", dad, "and mum is ", mum)
    
// }
// askAge(34)



// ___________________ Exercise 2_______________________________

// 1. Create a structured html file linked to a js file

// 2. Write a JS function that takes a parameter: myAge

// 3. Return the age of my mum (my mum is twice my age)

// 4. Call the function

// 5. Console.log the age of my mum

function mumAge (myage){
    let mum = "My madre is" + myage*2
    return mum
}
console.log(mumAge(prompt("what s your age")))




//defining a function

// FOR OF (generaly for array )

// function workingWithArray (list, name) {
//     console.log(list)
//     for(color of list){
//         console.log(name,  "loves the color", color)
//     }
// }

// //calling a function
// workingWithArray("blue", "red", "yellow"], "David")


// LOOP FOR IN (generaly for object)

// function workingWithArray (list, name) {
//     console.log(list)
//     for(color in list){
//         console.log(name,  "loves the color", list[color])
//     }
// }

// workingWithArray(["blue", "red", "yellow"], "David")

// functions nameFunction (paramater1, paramater 2)

// // call function
// nameFunction(argument, argument)

// IMPORTANT TO NOTE:
// the paramaters int he function definition(top) doenst matter so much, 
// they are ref for us to know- they are like a place holder to be filede with twhat we will determin in the finction
// when we are colling it it's important 

// function /for loop are block

// GLOBAL: Every thing that isn't in a block 
// LOCAL: what is inside {}

// What is global can be acced in the local but local cant be accessed in the global

// RETURN inside a function can get me a local value >global by making it a result of a function