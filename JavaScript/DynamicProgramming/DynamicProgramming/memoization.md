# Dynamic Programming
## Memoization
In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls to pure functions and returning the cached result when the same inputs occur again. Memoization has also been used in other contexts (and for purposes other than speed gains), such as in simple mutually recursive descent parsing.[1] It is a type of caching, distinct from other forms of caching such as buffering and page replacement. In the context of some logic programming languages, memoization is also known as tabling.
https://en.wikipedia.org/wiki/Memoization#:~:text=In%20computing%2C%20memoization%20or%20memoisation,the%20same%20inputs%20occur%20again.

### Overview

A memoized function "remembers" the results corresponding to some set of specific inputs. Subsequent calls with remembered inputs return the remembered result rather than recalculating it, thus eliminating the primary cost of a call with given parameters from all but the first call made to the function with those parameters. The set of remembered associations may be a fixed-size set controlled by a replacement algorithm or a fixed set, depending on the nature of the function and its use. A function can only be memoized if it is referentially transparent; that is, only if calling the function has exactly the same effect as replacing that function call with its return value. (Special case exceptions to this restriction exist, however.) While related to lookup tables, since memoization often uses such tables in its implementation, memoization populates its cache of results transparently on the fly, as needed, rather than in advance.

Memoized functions are optimized for speed in exchange for a higher use of computer memory space. The time/space "cost" of algorithms has a specific name in computing: computational complexity. All functions have a computational complexity in time (i.e. they take time to execute) and in space.

Although a space–time tradeoff occurs (i.e., space used is speed gained), this differs from some other optimizations that involve time-space trade-off, such as strength reduction, in that memoization is a run-time rather than compile-time optimization. Moreover, strength reduction potentially replaces a costly operation such as multiplication with a less costly operation such as addition, and the results in savings can be highly machine-dependent (non-portable across machines), whereas memoization is a more machine-independent, cross-platform strategy.


## Memoization Algorithm
1. Make it Work
- Visulize the problem as a tree
- implement the tree using recursion
- test it

2. Make it Efficient
- add in memo object
- add a base case to return memo values
- store return values into the memo