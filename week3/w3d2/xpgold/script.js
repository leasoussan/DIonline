// Exercise 1 : Select A Kind Of Music


// Show the value and the text of the selected option.
// Add an option: <option value="classic">Classic</option>.
// Make it selected.


// To select the value of a selected option 

// let selection = document.querySelector("select")

// let selectdrop=selection.options[selection.selectedIndex].value;

// console.log(selectdrop)


// let add =document.createElement("option")

// add.setAttribute("value", "classic")
// add.innerHTML="Classic"
// add.setAttribute("selected", "selected")
// selection.appendChild(add)


// let removeSelect = selection[1].removeAttribute("selected")
// console.log(removeSelect)





// Exercise 2: Delete Colors

// Create a function called : removecolor() that removes the selected color from the dropdown list.

// function removecolor(){
//     let selectcolor= document.getElementById("colorSelect");
//     selectcolor.remove(selectcolor.selectedIndex);
// }

// removecolor()




// Exercise 3 : Create A Shopping List
// Type what you need to buy on a text input field.
// Click on the “Add” button to add the item to your list.
// Click on the “Clear All” button to remove all items from the list.
// Click on the “Number of items” button to show the number of items in your list.
// The one and only element on the HTML file is :

// //reaching to the root- creat input place holder
// let shooping = document.getElementById("root");
// let list = document.createElement("input");
// list.setAttribute("type", "text");
// list.setAttribute("onfocus", "this.value=''");
// // this is to get a clear input after adding 


// shooping.append(list)
// // console.log(list)

// //adding button and accessing it
// let add = document.createElement("button")
// add.innerHTML = "add"
// add.setAttribute("id", "button")
// shooping.appendChild(add)

// console.log(add)


// let addTolist = document.getElementById("button");

// function addingOn() {
        
//         for (i = 0; i< shooping.length ; i++);
//         let item = document.createElement("li");
//         item.innerHTML= document.querySelector("input").value;
//         // item.innerHTML = list.value; works as well
//         shooping.appendChild(item);
// };


// addTolist.addEventListener('click', addingOn);


// //adding resset Button 
// let reset = document.createElement("button");
// reset.innerHTML = "reset"
// reset.setAttribute("id", "button2")
// shooping.appendChild(reset)

// console.log(reset)




// /////now calling button reste then finction then event Listener


// function clearAll(){
//     let oldList = document.getElementsByTagName("li");    
//     oldList.shooping.removeChild(oldList);
//     // while (oldList.hasChildNodes()) {  
//     //     oldList.removeChild(oldList.firstChild);
//     //   }
// };


// let resetList= document.getElementById("button2");

// //tel the button what todo 
// resetList.addEventListener('click', clearAll);


// ------SOLUTION------------------------------
//creating the variable in a global scoop then we wont need to do let name = blabla in the finction 
//just to call them 
let div;
let inputname;
let inputnumber;
let button;

let shooping = {};

function createElements(){
    //fetching the div
    div =document.getElementById("root")
    //creat the form 
    let form = document.createElement("form")
    //creat lable
    let lablename = document.createElement("lable")
    lablename.innerHTML = "Name of item"
    let lablenumber = document.createElement("label")
    lablenumber.innerHTML = "number of item"


    //creat the input as we declared the variable in the top no need to d it again -just to call it 
    inputname = document.createElement("input")
    inputname.setAttribute ("type", "text")
    inputnumber = document.createElement("input")
    inputnumber.setAttribute("type", "text")

    //creat button
    button = document.createElement("button")
    button.innerHTML="click"

    //append all in the form 
    form.appendChild(lablename)
    form.appendChild(inputname)
    form.appendChild(lablenumber)
    form.appendChild(inputnumber)
    form.appendChild(button)

    //appen the div to the page
    div.appendChild(form)


};

createElements()


// //creat event listene button 
// // when we click on the button the function fetchElement is called
// button.addEventListener("click", fetchElement)

// //calling the fnction when clickedd
function fetchElement(event){
    //to avoid the page to reload/refresh -to eventlistener
    event.preventDefault()
    // create a variable called inputnamevalue
    // and we assign to the variable inputnamevalue, the value of the input that we created in the function above
    let inputNamevalue = inputname.value
    // create a variable called inputnumber
    // and we assign to the variable inputnamevalue, the value of the input that we created in the function above
    let inputNumbervalue = inputnumber.value
    //goal is to add the quantity to an item inside the shooping list
    // calling the object and pusshing the property to the Object
    //object is in pair so we need to assigne the value to the new property 
    // shoopingList {
        // inputNamevalue: inputNumbervalue
    // }
    shopping[inputNamevalue]=inputNumbervalue
    console.log("shooping:", shooping)

}