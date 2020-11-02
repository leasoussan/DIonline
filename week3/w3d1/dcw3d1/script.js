// alert("daily Challenge week3 day1 ")

// This webpage is just a blank universe, and you’ll fill it with planets and moons in this challenge.
// You only have to work with a JS file

// Create an array of planets of the solar system
// For each planet, in the array, create a div using createElement. This div should have a class named ‘planet’.
// Each planet should have a different background color. (Hint: add a new class to each planet)
// Finally append each div to the body.
// Bonus Do the same process for moons. Be careful, each planet has a certain amount of moons; How should you display them ?
// <!DOCTYPE html>


var array= document.querySelector("body")

var listp =["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Planet Nine", "Pluto",]

var div = document.createElement("div")
for (i = 0; i < listp.length; i++){   
    var planet = document.createElement("div") //put each into a div
    planet.innerHTML= listp[i]
    div.appendChild(planet)
    planet.className ="planet"
    planet.style = ".planet"
    planet.style.backgroundColor ="yellow"
}

console.log(div)


// /TODO Last question - cehck class results 