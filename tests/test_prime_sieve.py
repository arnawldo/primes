import pytest

from src.prime_generator import prime_sieve


def test__prime_sieve_returns_none_for_negative_input__succeeds():
    primes = prime_sieve(-3)
    assert primes is None


def test__prime_sieve_returns_empty_list_for_0_input__succeeds():
    primes = prime_sieve(0)
    assert primes == []


def test__prime_sieve_returns_correct_output__succeeds():
    primes = prime_sieve(6)
    assert primes == [2, 3, 5]


def test__prime_sieve_returns_n_inclusive_if_prime__succeeds():
    primes = prime_sieve(7)
    assert primes == [2, 3, 5, 7]


def test__prime_sieve_str_input__raises():
    with pytest.raises(TypeError):
        primes = prime_sieve("7")

def test__prime_sieve_float_input__raises():
    with pytest.raises(TypeError):
        primes = prime_sieve(7.4)
