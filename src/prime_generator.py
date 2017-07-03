def prime_numbers(n):

    if n < 0:
        return None

    primes = []

    for i in range(2, n + 1):

        # assume number to be prime
        isPrime = True

        # all numbers from 2 to checked
        for j in range(2, i):

            # if we find number to be divisible, not prime
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(i)

    return primes