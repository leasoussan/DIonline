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

//reaching to the root- creat input place holder
let shooping = document.getElementById("root");
let list = document.createElement("input");
list.setAttribute("type", "text");
list.setAttribute("onfocus", "this.value=''");
// this is to get a clear input after adding 


shooping.append(list)
// console.log(list)

//adding button and accessing it
let add = document.createElement("button")
add.innerHTML = "add"
add.setAttribute("id", "button")
shooping.appendChild(add)

console.log(add)


let addTolist = document.getElementById("button");

function addingOn() {
        
        for (i = 0; i< shooping.length ; i++);
        let item = document.createElement("li");
        item.innerHTML= document.querySelector("input").value;
        // item.innerHTML = list.value; works as well
        shooping.appendChild(item);
};


addTolist.addEventListener('click', addingOn);


//adding resset Button 
let reset = document.createElement("button");
reset.innerHTML = "reset"
reset.setAttribute("id", "button2")
shooping.appendChild(reset)

console.log(reset)




/////now calling button reste then finction then event Listener


function clearAll(){
    let oldList = document.getElementsByTagName("li");    
    oldList.shooping.removeChild(oldList);
    // while (oldList.hasChildNodes()) {  
    //     oldList.removeChild(oldList.firstChild);
    //   }
};


let resetList= document.getElementById("button2");

//tel the button what todo 
resetList.addEventListener('click', clearAll);
