# Prime number generator
Generates prime numbers from 0 to given integer

Running time of algorithm is O(n^2)

*Explanation*
* Outer for loop runs approx `n` times ie `range(2, n)`  
* Inner loop runs approx n times as well because `range(2, i)` is generated at least `n` times
* That makes quadratic running time `(n * n)`

