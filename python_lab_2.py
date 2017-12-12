# -*- coding: utf-8 -*-
""" Repaso interactivo de python
"""
from typing import List
from typing import Tuple


def lower_up(lower: int, upper: int) -> None:
        """ 1: Returns a list of numbers from the lower number to the upper number:
        >>> lower_up(5,15)
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        """
        for x in range(lower, upper + 1):
            print(x)


def all_the_args(*args, **kwargs):
    """ 2: Return an array. Use * to expand positional args
    and use ** to expand keyword args
    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {'a': 3, 'b': 4}
    """
    print(args)
    my_dict = {}
    keys = kwargs.keys()
    keys = reversed(sorted(keys))  # order them in some way
    for k in keys:
        my_dict[k] = kwargs[k]
    print(my_dict)


def may_20(tup: Tuple[int]) -> None:
    """ 3: Definir una tupla con 10 números.
    Imprimir la cantidad de números superiores a 20.
    >>> may_20((10, 16, 22, 26, 27, 30))
    22, 26, 27, 30
    """
    superiores = ""
    for x in tup:
        superiores = compara_20(superiores, x)

    print(superiores)


def compara_20(cad_temp: str, cadena: int) -> str:
    if cadena > 20:
        cad_temp = concatena(cad_temp, cadena)
    return cad_temp


def concatena(cad_temp: str, cadena: int) -> str:
    if cad_temp == "":
        cad_temp = str(cadena)
    else:
        cad_temp = cad_temp + ", " + str(cadena)
    return cad_temp


def word_filter(list_of_words, n):
    """ 4: Filtra las palabras que contienen más de n caracteres.
    >>> word_filter(['hello','bye', 'computer', 'software', 'python'], 5)
    ['computer', 'software', 'python']
    """
    lists = []
    for item in list_of_words:
        len_calculator(item, n, lists)
    print(lists)


def len_calculator(item: str, n: int, lists: List[str]) -> None:
    if len(item) > n:
        lists.append(item)


def string_length(list: str) -> None:
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
    10
    """
    print(len(list))


def is_vocal(x: str) -> None:
    """ 6: Determines if it is vocal
    >>> is_vocal('a')
    True
    >>> is_vocal('c')
    False
    """
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        print(True)
    else:
        print(False)


def is_leap_year(year: int) -> None:
    """ 7: Determines if a year is a leap year.
    >>> is_leap_year(2016)
    True
    """
    if year % 400 == 0:
        print(True)
    helper_is_leap_year_second_condition(year)


def helper_is_leap_year_second_condition(year: int) -> None:
    if year % 4 == 0 and year % 100 != 0:
        print(True)
    else:
        print(False)


def has_uppercase(word: str) -> None:
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase("MayuSculA")
    3
    """
    print(sum(1 for i in word if i.isupper()))


def contar_vocales(cadena: str) -> None:
    """ 9: Return number of vocales in a word.
    >>> contar_vocales('murcielago')
    5
    """
    sum = 0
    for x in cadena:
        sum += is_vowel(x)
    print(sum)


def is_vowel(x: str) -> int:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return 1
    else:
        return 0


def square(lists: List[int]) -> None:
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    # print(list(1 for i in x if i.isupper()))
    print(list(map(lambda x: x**2, lists)))


def is_prime(n: int) -> None:
    """ 11:  Return if n is prime.
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if n > 1:
        is_prime_helper(n)


def is_prime_helper(n: int) -> None:
    for i in range(2, n):
        is_prime_comparison(n, i)
        break
    else:
        print(False)


def is_prime_comparison(n: int, i: int) ->None:
    if (n % i) == 0:
        print(False)
    else:
        print(True)


def factorial(n: int) -> int:
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    """
    result = 1
    factor = 2
    # if n == 0:
    #    return 1
    # else:
    #    return n * factorial(n-1)
    while factor <= n:
        result *= factor
        factor += 1
    return result


def to_roman(n: int) -> str:
    val = (1000, 900,  500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
           'V', 'IV', 'I')
    roman_num = ""
    list = []
    for i in range(len(val)):
        count = int(n / val[i])
        roman_num += syb[i] * count
        n -= val[i] * count
    list.append(roman_num)
    return str(list).replace("'", "")


def rima(word1: str, word2: str) -> None:
    """ 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima,
    si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
    >>> rima('flor', 'coliflor')
    rima
    >>> rima('amar', 'plantar')
    rima un poco
    >>> rima('azucar', 'barrer')
    no rima
    """
    if word1[len(word1) - 1] == word2[len(word2) - 1]:
        rima3(word1, word2)
    else:
        print('no rima')


def rima3(word1: str, word2: str) -> None:
    if word1[len(word1) - 2] == word2[len(word2) - 2]:
        rima2(word1, word2)
    else:
        print('no rima')


def rima2(word1: str, word2: str) -> None:
    if word1[len(word1)-3] == word2[len(word2)-3]:
        print('rima')
    else:
        print('rima un poco')


def capital(pesos: int, interes: float, anios: int) -> None:
    """ 15: Pide una cantidad de pesos, una tasa de interés y un
    número de años. Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada año se
    aplica la tasa de interés introducida.
    >>> capital(10000, 4.5, 20)
    24117.14
    """
    resultado = pesos * (1 + interes / 100) ** anios
    print(round(resultado, 2))
