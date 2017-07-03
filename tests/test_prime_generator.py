import pytest

from src.prime_generator import prime_numbers


def test__prime_numbers_returns_none_for_negative_input__succeeds():
    primes = prime_numbers(-3)
    assert primes is None
