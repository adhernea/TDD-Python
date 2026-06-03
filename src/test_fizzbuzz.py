import pytest

from main import fizz_buzz


def test_when_zero_give_empty_string():
    assert fizz_buzz(0) == ""

def test_when_one_give_empty_string():
    assert fizz_buzz(1) == ""

def test_when_three_give_fizz():
    assert fizz_buzz(3) == "Fizz"

def test_when_five_give_buzz():
    assert fizz_buzz(5) == "Buzz"

def test_when_fifteen_give_fizzbuz():
    assert fizz_buzz(15) == "FizzBuzz"

def test_when_22_give_same():
    assert fizz_buzz(22) == 22
