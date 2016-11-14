'''Połącz wszystkie slowa w liscie l = ['a', 'b', 'c', 'd'] '''

'''Stwórz listę dwuwymiarową za pomocą pętli t = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] '''

'''
Walidacja email:
- zawiera @
- przed @ sa 3 znaki
- conajmniej jeden znak po @ następnie kropka i nastepnie conajmniej jeden znak
'''

'''
Stworz słownik którego kluczami będą imiona np Jaś, Jan, Adam, a ich wartoścami
ich wiek np. [10, 15, 20]

Wypisz osobę o wieku 15
'''

'''
Program wczyta tekst od użytkownika i wypisze jego tekst w ramce

*******************
* HELLO STRANGER! *
*******************
'''

'''
Wypisz co drugi znak ze stringu wprowadzącego przez użytkownika
'''

'''
Wypisz tylko cyfry ze stringu s = 'asdj3hj429f29103'
'''

'''
Posortuj liste po drugim elemencie
'''
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (1, 1), (20, 5)]

'''
Stworz liste skladajaca sie tylko z liczb parzystych mniejszych od 30
'''


'''
ZADANIE DLA CHĘTNYCH/BARDZIEJ ZAAWANSOWANYCH Z GWIAZDKĄ -> *

napisz ciało funkcji rotate_array (pod treścią zadania) która

1) jako argument przyjmuje tablice 2wymiarową oraz opcjonalnie liczbę obrotów które wykonać
    (btw, nowa rzecz, defaulty w argumentach funkcji)
2) zwraca tablicę obróconą o 90stopni * ilość obrotów do wykonania (default 1)

dopisałem wam metodę do wyświetlania tablic i jakieś przykładową tablice do testów
jak odpalicie ten plik używając

python3 homework.py

to będziecie testować swoje rozwiązanie. Narazie powinno wam wyświetlić testowe tablice
a potem rzucić TypeError bo rotate_2d_array nie zwraca nic (pass w pythonie to słowo kluczowe
które mówi pythonowi że sorrka ale narazie chillujemy i nic nie robimy w tym miejscu :) więc python widzi None)

'''

def rotate_2d_array(array, num_of_rotations=1):
    pass

def print_2d_array(array):
    for row in array:
        print(' '.join(str(_) for _ in row))


TESTS = [
    [
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 1, 0],
    ],
    [
        [1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
    ],
]

if __name__ == '__main__':

    print("tests:")
    for arr in TESTS:
        print("\n")
        print_2d_array(arr)
        print("\n*****")

    for rotations in range(1,4):
        print("results after %s rotation:" % (rotations,))
        for arr in TESTS:
            print_2d_array(rotate_2d_array(arr, rotations))

