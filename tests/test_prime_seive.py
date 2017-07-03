import pytest

from src.prime_generator import prime_seive


def test__prime_seive_returns_none_for_negative_input__succeeds():
    primes = prime_seive(-3)
    assert primes is None


def test__prime_seive_returns_empty_list_for_0_input__succeeds():
    primes = prime_seive(0)
    assert primes == []


def test__prime_seive_returns_correct_output__succeeds():
    primes = prime_seive(6)
    assert primes == [2, 3, 5]


def test__prime_seive_returns_n_inclusive_if_prime__succeeds():
    primes = prime_seive(7)
    assert primes == [2, 3, 5, 7]


def test__prime_seive_str_input__raises():
    with pytest.raises(TypeError):
        primes = prime_seive("7")

def test__prime_seive_float_input__raises():
    with pytest.raises(TypeError):
        primes = prime_seive(7.4)
