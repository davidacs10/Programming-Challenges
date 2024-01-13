### Fizz Buzz Challenge ###

#  * Dificultad: FÁCIL
#  * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

lst = list(range(1, 101))

for number in lst:
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: FizzBuzz")
    elif number % 3 == 0:
        print(f"{number}: Fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(number)