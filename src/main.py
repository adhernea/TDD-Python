print('Hello world!')

def fizz_buzz(number: int):
    if number == 0 or number == 1:
        return ""
    
    if number%3 == 0 and number%5 == 0:
        return "FizzBuzz"
    elif number%3 == 0:
        return "Fizz"
    elif number%5 == 0:
        return "Buzz"
    
    return number
    