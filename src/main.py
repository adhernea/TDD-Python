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
    Ejercicio 1. Esta función recoge una cadena de texto de números enlazados con comas y devuelve la suma resultante de los mismos.
    
    Ejercicio 2. Esta función recoge una cadena de texto de números enlazados con un delimitador y devuelve la suma resultante de los mismos.
    El delimitador se indica al inicio de la cadena de texto con // y luego la cadena de números tras una barra.
    Por ejemplo:
        //,\n1,2,3     -> 6
        //;\n3;4;5     -> 12
        //::\n1::1::1  -> 3
"""
def sum_delimiter_collection(text: str):

    if isinstance(text, int):
        return text
    elif isinstance(text, list):
        return -1

    numbers_str: [str] = text.split(',')

    total_sum = 0

    for numbstring in numbers_str:
        try:
            total_sum += int(numbstring)
        except:
            return 0
    
    return total_sum

