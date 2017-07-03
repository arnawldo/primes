# Prime number generator

Running time of algorithm is O(n^2)

*Explanation*
* Outer for loop runs approx `n` times ie `range(2, n)`  
* Inner loop runs approx n times as well because `range(2, i)` is generated ar least `n` times
* Thats makes quadratic running time `(n * n)`

