'''
Stwórz listę liczb parzystych za pomocą list comprehension

l = [x for x in range(5) if x%2 == 0]

'''

'''
Mając dwie listy ['a', 'b', 'c'] i [1, 2, 3]
stwórz słownik używając dict comrehension
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

d = {key: value for key, value in zip(l1, l2)}

'''

'''
Napisz funkcję która przyjmując dwa argumenty zachowa się inaczej dla
stringów a inaczej dla liczb, gdy są to liczby spróbuje je podzielić (pamiętaj o
dzieleniu przez 0), a gdy są to stringy powinna je dodać

def iterating_list(a , b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Nie można dzielić przez 0 !'
    except TypeError:
        return a + b

'''


'''
Napisz generator który będzie działał jak range(n) który zwraca kolejną liczbe)

def gen(n):
    x = 0
    while x < n:
        yield x
        x += 1

'''

'''
Napisz klasę Cat and Dog, niech obie przyjmują jeden argument podczas tworzenia
i będzie ich to imie, zaimplementuj metode która będzie wypluwać ich imie, ale
nie powielaj kodu

class Animal:
    def __init__(self, name):
        self.name = name

    def do_sound(self):
        print(self.name)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

'''

'''
***Stwórz klasę bez użycia keword class
new_cls = type("my_cls", (), {})
'''
