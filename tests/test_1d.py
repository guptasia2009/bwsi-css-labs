"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_example_case():
    assert two_sum([2, 7, 11, 15], 9) ==[0, 1]

def test_reverse_order():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

if __name__ == "__main__":
    pytest.main()