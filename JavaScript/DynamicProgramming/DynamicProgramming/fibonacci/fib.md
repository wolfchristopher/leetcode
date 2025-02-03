# Dynamic Programming

https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1206s 

## Fibonacci

Write a function `fib(n)` that takes in a number as an argument. The function should return the n-th number of the Fibonaci sequence.

The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.

    n:      1, 2, 3, 4, 5, 6, 7, 8, 9, ...
    fin(n): 1, 2, 2, 3, 5, 8, 13, 21, 34, ...

The implementation of the classic Fibonacci sequence in JavaScript using recursion:

```
const fib = (n) => {
    if (n <= 2) return 1;
    return fib(n - 1) + fib(n - 2)
}

console.log(fib(6))
console.log(fib(7))
console.log(fib(8))
console.log(fib(50))
```

In this example you would be brute forcing the solution as the big O notation for this solution would be O(2^n)

### So why does this have a O(2^n) time complexity?

Lets look at this Foo Function:
```
const foo = (n) => {
    if (n <= 1) return;
    foo(n-1);
};
```
It's similar in that it is recursive. It does not solve a particular problem. Lets call the function with foo of 5 at the top level.
```
foo(5)
```
So its goin I know five is not a base case. So it's going to call upon n minus one, or it's
going to call upon for four calls three, three calls to two calls one, and then here, we've
actually bottomed out at a base case. If you look at the number of calls I made, I basically made exactly five function calls.

Which makes sense, because in terms of our base case, where do we stop once we hit a number less than or equal to one and every recursive step, we just subtract one from our current value of n. So overall, I have five calls here.

But if I generalize that, for any arbitrary input, I know that in the long run, I'm going to have about n different function calls recursively. And so for that reason, the time complexity of this is really just O of n time, right? I have to evaluate O of n different function calls. 


While we're at it, why don't we take a look at the space complexity? Well, you may have heard in past that when we analyze the space complexity of our recursive functions, we should include any of the additional stack space that our function calls take up right, when we make a recursive call, we add that to the call stack, and those must be tracked by our computer. And so since we have about five or n different function calls added to
the stack, before we hit our base case, you can see that the space complexity of this code is also O of n space, overall, we're looking at O of n time and open space for this function

![Foo Big(O)](./foo_big(O).png)

Let's look at another more involved function. It's similar to foo() but the only difference is when you make the recursive call, we do an n - 2 instead of 1.


```
const bar = (n) => {
    if (n <= 1>) return;
    bar(n-2);
};
```
So how does that actually change the time complexity of this function?



```
const lib = (n) => {
    if (n <= 1) return;
    lib(n-2);
    lib(n-2);
};
```




This pattern of overlapping subproblems is known as dynamic programming.