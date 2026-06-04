print('Hello world!')

"""
    Esta función recibe un número entero y devuelve Fizz si el número es múltiplo de 3, Buzz si es múltiplo de 5 y FizzBuzz si es múltiplo de ambos.
    En caso de tener una entrada de 1 o 0 retornará un string vacío.
    En caso de pasar un número que no sea ningún múltiplo de 3 o 5 retornará el número en cuestión.
"""
def fizz_buzz(number: int):
    if not isinstance(number, int) or number == 0 or number == 1:
        return ""
    
    if number%3 == 0 and number%5 == 0:
        return "FizzBuzz"
    elif number%3 == 0:
        return "Fizz"
    elif number%5 == 0:
        return "Buzz"
    
    return number


"""
    Esta función recoge una cadena de texto de números enlazados con comas y devuelve la suma resultante de los mismos.
"""
def sum_comma_collection(text: str):
    pass