"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_example_case():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_negative():
    assert max_subarray_sum([-5, -1, -8]) == -1

def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10

if __name__ == "__main__":
    pytest.main()