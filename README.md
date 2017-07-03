# Prime number generator

## Function: `prime_numbers`
Generates prime numbers from 0 to given integer

Running time of algorithm is O(n^2)

*Explanation*
* Outer for loop runs approx `n` times ie `range(2, n)`  
* Inner loop runs approx n times as well because `range(2, i)` is generated at least `n` times
* That makes quadratic running time `(n * n)`

## Function: `prime seive`
Generates prime numbers from 0 to given integer using Seive of Eratosthenes algorithm.   

Running time of algorithm is `O(n*log(log(n)))`

*Explanation*  
The algorithm goes through multiples of all the primes and marks them as non prime.

``T(n) = n/2 + n/3 + n/5 ... = n * (sum of reciprocals of primes up to n)``  
[Divergence of the sum of the reciprocals of the primes ](https://www.wikiwand.com/en/Divergence_of_the_sum_of_the_reciprocals_of_the_primes)