import pytest

from main import fizz_buzz


def when_zero_give_empty_string():
    assert fizz_buzz(0) == ""

def when_one_give_empty_string():
    assert fizz_buzz(1) == ""

