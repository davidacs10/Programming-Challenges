### Prime number Challenge ###

"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():

    # Este ciclo recorre cada número del 1 al 100 (inclusive).
    for number in range(1, 101):

        # Esta condición asegura que solo se comprueben los números mayores o iguales a 2 para ver si son primos. El 1 no es primo, por eso se excluye.
        if number >= 2:

            # Esto inicializa una bandera asumiendo que el número es primo (no es divisible por ningún otro número) hasta que se demuestre lo contrario.
            is_divisible = False
        
            # Este ciclo interno recorre los números del 2 hasta (pero sin incluir) el number actual. Está buscando divisores potenciales.
            for i in range(2, number):

                # Si el number es divisible por i (el resto es 0), significa que no es primo.
                if number % i == 0:

                    # Si el número es divisible por i, esta bandera se pone a True, indicando que no es primo.
                    is_divisible = True

                    # El ciclo interno se detiene aquí porque ya se encontró un divisor, no es necesario seguir buscando.
                    break
            
            # Si el número no ha sido marcado como divisible por ningún otro número, significa que es primo.
            if not is_divisible:
                print(number)

is_prime()