// alert("daily Challenge w2d3")

// Daily Challenge : Bubble Sort

let numbers = [5,0,9,1,7,4,2,6,3,8];


// Using the .toString() method, convert the array to a string.
let str = numbers.toString()

// console.log(numbers.toString())
console.log(str)

// Using the .join(), convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)

let string = numbers.join(" () ");
console.log(string)

// Bonus : Sort the array numbers in descending order using for loops (Not using built-in sort methods).
// The output should be: [9,8,7,6,5,4,3,2,1,0]
// Hint: The algorithm is called “Bubble Sort”

// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Add comments and console.log the result for each step, it will help you understand.
// Requirement: Don’t copy paste solutions from Google

// let numbers = [5,0,9,1,7,4,2,6,3,8];

// function bubbleSort(numbers){
//     let length= numbers.length

//     for (i = 0; i < length; i--){
//         for(j=0; j<length - i -1; j--){
//             if (numbers[j]< numbers[j-1]){
//                 let temporary = numbers[j];
//                 numbers[j] = numbers[j-1];
//                 numbers[j-1]= temporary;}
//             }
//         }
//     }    
// console.log(bubbleSort)




