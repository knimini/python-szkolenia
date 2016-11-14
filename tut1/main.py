
def main():
    # Sum the list!
    lista = [23, 54, 74, 12, 89, 89, 78, 56, 4, 2, 4]

    # C style
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]

    # Python iteration style
    suma = 0
    for liczba in lista:
        suma += liczba

    # Functional programming style
    from functools import reduce
    out = reduce(lambda x,y: x+y, lista)

    # \o/
    suma = sum(lista)

    print (suma)

if __name__ == '__main__':
    main()
