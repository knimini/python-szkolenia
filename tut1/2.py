# Check if element is in a collection
def isElement(elem, iterable):
    for i in range(len(iterable)):
        if elem == iterable[i]:
            return True
    return False


def isElement1(elem, iterable):
    for i in iterable:
        if elem == i:
            return True
    return False


def isElement2(elem, iterable):
    return elem in iterable


def main():
    elem = 1
    numerki = [1, 2, 3, 5, 7, 24, 12]
    print(isElement(elem, numerki))
    print(isElement1(elem, numerki))
    print(isElement2(elem, numerki))

    slownik = {1:"one", 2:"two", 3:"three", 5:"five", 7:"seven", 24:"twenty-four", 12:"twelve"}
    print(isElement(elem, slownik))
    print(isElement1(elem, slownik))
    print(isElement2(elem, slownik))


if __name__ == '__main__':
    main()
