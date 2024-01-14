### Anagram Challenge ###


#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

def is_anagram(string_1, string_2):
    string_1 = string_1.lower().replace(" ", "")
    string_2 = string_2.lower().replace(" ", "")
    
    if len(string_1) != len(string_2) or string_1 == string_2:
        return False

    return sorted(string_1) == sorted(string_2)



print(is_anagram("Roma", "Amor"))