// Functions in JavaScript
// Q1 - What is Function Declarations?

function add(number) {
    return num + num
}

// Q2 - What is Function Expression?
const square = function (num) {
    return num * num
}


// Q3 - What are first class functions?
function displaySquare(fn) {
    console.log("Square is " + fn())
}


// Q4 - What is IIFE?
//Immediately invoked function expressions
(function add(number) {
    return num + num
})(5);


// Q5 - IIFE - O/P Based Question?
(function (x) {
    return (function (y) {
        console.log(x) // 1
    })(2)
})(1)


// Q6 - Function Scope

//Function Scope
// Variables defined inside a function cannot be accessed from anywhere outside the function, because the variable is defined only in the scope of the function. However, a function can access all variables and functions defined inside the scope in which it is defined.

// In other words, a function defined in the global scope can access all variables defined in the global scope. A function defined inside another function can also access all variables defined in its parent function, and any other variables to which the parent function has access.

// The following variables are defined in the global scope
const num1 = 20;
const num2 = 3;
const name = "Chamakh";

// This function is defined in the global scope
function multiply() {
    //It goes and looks in local scope first and then goes and looks at its parents scope for the variable.
  return num1 * num2;
}

multiply(); // Returns 60

// A nested function example
function getScore() {
  const num1 = 2;
  const num2 = 3;

  function add() {
    return `${name} scored ${num1 + num2}`;
  }

  return add();
}

getScore(); // Returns "Chamakh scored 5"


// Q7 - Function Scope - O/P Based Question
/// let has a block scope to allow access while var doesn't.
for (let i = 0; i < 5; i++) {
    setTimeout(function () {
        console.log(i)
    }, i * 1000)
}
// Q8 - Function Hoisting