// Development logic of function:
// 1. I want to prompt a number from user
// 2. I would like to enter a loop that is decreasing 
// 3. every tim the loop godown the number of decreasing goes up until there is no more bottle
// 4. change when we get to one bottel make correction




// get number 
 getnbr = prompt("How many beers are you at");
 let beers = getnbr;

// max number of bottle

let end = false

let increment = 1
    while (beers > 0){
        increment++;
    }

let decrease = increment(1);

let numBeers = 99 - decrease;


function countDown (bottle){
    while (beers > 0){
        beers = beers - decrease;  
        console.log(beers + "bottles of beer on the wall");
        console.log("take" + increment + "down and passe them down");    
        }
        if (beers == 1){
            console.log("take One and passe it down")
        } else if (beers = 0){
            console.log("there are no more beers...you are drunk");
    
        }
    if (beers > 99){
        alert("there are only 99 bottle You can't go over this")
    }else (getnbr);
    }

console.log(countDown(getnbr))
