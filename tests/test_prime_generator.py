import pytest

from src.prime_generator import prime_numbers


def test__prime_numbers_returns_none_for_negative_input__succeeds():
    primes = prime_numbers(-3)
    assert primes is None

def test__prime_numbers_returns_correct_output__succeeds():
    primes = prime_numbers(6)
    assert primes == [2, 3, 5]

def test__prime_numbers_returns_n_inclusive_if_prime__succeeds():
    primes = prime_numbers(7)
    assert primes == [2, 3, 5, 7]

def test__prime_numbers_str_input__raises():
    with pytest.raises(TypeError):
        primes = prime_numbers("7")