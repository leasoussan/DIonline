//  alert("week 2 day 3 - XP GOLD -WELCOME")

// Exercise 1 : Attendance
// Suppose you have a guest list of students and the country they are from, stored as key-value pairs in an object. You have to make the attendance.

// 
// Ask the student for his name :
// If the name is in the object, console.log the name of the student and the country he comes from.
// "Hi! I'm [name], and I'm from [country]."
// If the name is not in the object, console.log :"Hi! I'm a guest."
// 


let name = prompt("what si your name?")

let guestList = {
      Randy: "Germany",
      Karla: "France",
      Wendy: "Japan",
      Norman: "England",
      Sam: "Argentina"
}
    
      if(name in guestList){
        console.log("Hi! I'm " + name + "and I'm form "+ guestList[name]);
      }
        else{console.log("hello Im a guest")};

// Other Ex to understand before commiting


        // let guestList = {
        //   Randy: "Germany",
        //   Karla: "France",
        //   Wendy: "Japan",
        //   Norman: "England",
        //   Sam: "Argentina"
        // }
        // let username = prompt("what is your name?")
        // for (let name in guestList) {
        //     if (username == name ){
        //     console.log("Hi! I'm, " + names + " and I'm from " + guestList[username] + ".")
        //     } else {
        //         console.log("Hi! I'm a guest.")
        //     }
        // }
        

  // let [key, value] of Object.entries(guestList) {
  //     console.log(`Hi I am ${key} and am from  ${value}`);
  //   }
  
  //   let names = Object.entries(guestList)
  //   console.log(names)

  //   // to access the countries
  // let country = (Object.values(guestList))
  // console.log(country)

// COMMENT
//   There are 2 ways to call a property in a object 
//   object.property or object[variable or "name"]

//   forex here to console.log(name) === names
//   consol log counties >> console.log[guestList[name]]

  // for (g = 0; g< guest.lenght ; g++){
  // } console.log("hi Iam " + guest + " and I am from" + countr

  











// Exercise 2 : Family
// Create an object called family with a few properties.
// Display only the properties.
// Display only the values.
// 





// Exercise 3 : Building Management
// let building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 990],
//         "Dan":  [4, 1000],
//         "David": [1, 500],
//     },
// }
// Display the number of levels in the building.
// Display how many apartments are on level 1 and 3.
// Display the name of the second tenant and the number of rooms he has in his apartment.
// Check if the rent of Sarah plus the rent David is bigger than the rent of Dan.
// If it is than ask the owner to increase Dan’s rent (ask him for a new amount).
// Change the rent of Dan accordingly inside the object.
// Exercise 4 : Checking The BMI
// Create two objects, each one should hold a person details. Here are the details: fullName, mass, height.
// Each object should also have a property which value is a function that calculates the Body Mass Index (BMI) of each person
// Create a JS function that compare both the BMI. Display the name of the person that has the biggest BMI.
