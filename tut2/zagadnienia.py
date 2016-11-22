'generatory wyjatki list comperhensions klasy'
'''
List comperhension
'''
l = []
for i in range(5):
    l.append(i**2)

l = [x**2 for x in range(5)]

zdanie = 'Chciałbym aby te zdanie było w uppercase'
nowe_zdanie = ''
for slowo in zdanie.split():
    nowe_zdanie += slowo.upper() + ' '

nowe_zdanie = ' '.join(slowo.upper() for slowo in zdanie.split())
'''
stworzyć listę kolejnych potęg 2

'''

'''
Exceptions
'''

try:
    10/0
except ZeroDivisionError:
    print('Nie można dzielić przez 0')


def divide(a, b):
    try:
        print(a/b)
    except TypeError as e:
        print(e)

'''
input: [1, 2, 3]
output: [1, 3, 5]
input: [a, b, c]
output: ['', 'b', 'cc']
'''


def iterating_list(seq):
    try:
        return [int(item) + it for it, item in enumerate(seq)]
    except ValueError:
        return [item * it for it, item in enumerate(seq)]

'''
Generators
'''


def simple_gen(n):
    for i in range(n):
        yield i
my_gen = simple_gen(5)
print(next(my_gen))

for val in my_gen:
    print(val)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

'''
Classes
overide magic methods
inheritance

'''

class Vehicle:
    def do_sound(self):
        print(self.sound)

class Car(Vehicle):
    sound = 'wrum wrum'

    def __init__(self, color):
        self.color = color


class Motorcycle(Vehicle):
    sound = 'brum brum'

    def __init__(self, color):
        self.color = color



