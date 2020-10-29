alert( "XP NINJA week3 day 3- good luck ")

// Exercise 1 : Grade Average
// Hint :
// - This Exercise is more tricky that the ones done before. You have to think about its structure before starting to code.
// - You can even make it better with your own ideas
// - If you want to improve it, do the exercises using Functions

// The point of the exercise is for a user to check his average, after his semester exams.
// It’s an european exam, so the way of calculating the average is with grades and coefficient.
// Before starting, look at this page to understand what a coefficient is

// Create a global object called average then,
// Ask the user to give you his name.
// Ask the user to give you a the name of the course (Ex: Maths, Physics, etc…). Save it in a variable.
// Ask the user to give you the grade that he thinks he will get for this specific course. Save it in a variable.
// Ask the user to give you the coefficient of this specific course. Save it in a variable.
// For these three first steps, continue asking for the questions until the user gives you an adequat and not empty answer.
// Create a local object called course that should contains the variables of the 3 first steps. Think about the structure of this object.
// Add the object course to the global object average.
// Then ask the user if he wants to continue the process with a new course, grade, and coefficient.
// If the answer is “Yes”, than continue the process above from question 1 to 6.
// If the answer is “No” than display him a message with his name and his semester average.
// Note: Calculation of the average ((Grade x Coefficient)/(Sum of all the Coefficient))
// Example :

// Maths - Grade: 80 - Coefficient : 4
// English - Grade: 60 - Coefficient : 2
// Average = (80x4 + 60x2)/4+2