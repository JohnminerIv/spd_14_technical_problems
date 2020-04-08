/*
orgiginal function
function FizzBuzz( targetnum)
{
    for (var i=1; i<targetnum; i++;) {
        let result = "";
        if (i%3 === 0) result += "Fizz";
        if (i%5 === 0) result += "Buzz";
        if (i%3 > 0 & i%5 > 0 ) result = i;
        console.log(result += '\n');
    }
}
FizzBuzz(50)
*/

// I don't really use javascript that often so I don't know conventions but
// this looks somewhat better 
function fizzBuzz(targetNum){
  for (var i = 1; i <= targetNum; i++){
    let result = "";
    if (i % 3 === 0){
      result += "Fizz"
    }
    if (i % 5 === 0){
      result += "Buzz"
    }
    if ((i % 3 > 0) & (i % 5 > 0 )){
      result = i
    }
    console.log(result += '\n');
  }
}
fizzBuzz(50)
