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

let shooping = document.getElementById("root");
let list = document.createElement("input");
list.setAttribute("type", "text");
list.setAttribute("placeholder", "enter items");

shooping.append(list)

console.log(list)


let add = document.createElement("button")
add.innerHTML = "add"
shooping.appendChild(add)

add.addEventListener("click", function(){
    add= document.querySelector("text");
    add.appendChild(list);
})


// function add() {
//     data.push({ name: userinput.value });
//     userinput.value='';
//     refresh();
//   }

