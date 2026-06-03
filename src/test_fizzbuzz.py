import pytest

from main import fizz_buzz


def when_zero_give_empty_string():
    assert fizz_buzz(0) == ""

def when_one_give_empty_string():
    assert fizz_buzz(1) == ""

def when_three_give_fizz():
    assert fizz_buzz(3) == "Fizz"

def when_five_give_buzz():
    assert fizz_buzz(5) == "Buzz"

def test_fizz_buzz_fifteen():
    assert fizz_buzz(15) == "FizzBuzz"

