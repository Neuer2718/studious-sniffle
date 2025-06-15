import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from prime_number_checker import is_prime

@pytest.mark.parametrize("n,expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (11, True),
    (15, False),
])
def test_is_prime_various(n, expected):
    assert is_prime(n) is expected
