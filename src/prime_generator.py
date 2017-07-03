def prime_numbers(n):

    """
    Given integer, generates prime numbers from 0 to stopping number
    :param n: stopping number
    :type n: int
    :return: list of prime numbers up to n
    :rtype: list
    """
    # return if input is negative
    if n < 0:
        return None

    primes = []

    for i in range(2, n + 1):

        # assume number to be prime
        is_prime = True

        # all numbers from 2 to checked number
        for j in range(2, i):

            # if we find number to be divisible, not prime
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes

def prime_sieve(n):
    """
    Generate prime numbers from 0 to given number using the Sieve of Eratosthenes algorithm
    :param n: stopping number
    :type n: int
    :return: list of prime numbers up to n
    :rtype: list
    """

    # return if input is negative
    if n < 0:
        return None

    not_prime = []
    primes = []

    for i in range(2, n + 1):
        if i not in not_prime:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                not_prime.append(j)

    return primes

