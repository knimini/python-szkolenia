for letter in "string": # Iteracja po elementach kolekcji
    print(letter)

for element in ["element", 20, 1.0, 2e4, (1, 20)]: # Iteracja po elementach kolekcji
    if type(element) == tuple:
        print("Found a tuple in the list")
        break # break powoduje przerwanie pętli

for element in ["element", 20, 1.0, 2e4]:
    if type(element) == tuple:
        print("Found a tuple in the list")
        break
else:
    print("No Tuple :(")

for element in ["element", 20, 1.0, 2e4]:
    if type(element) == tuple:
        continue # continue powoduje pominięcie reszty kodu w danej iteracji pętli
    print(element)
