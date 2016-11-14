n = 10

while True: # pętla wykonuje się tak długo jak warunek jest prawdziwy
    if not n%200 and n>200:
        break # wyjście z funkcji w momencie gdy spelnione sa warunki powyzej
    n += 1
    print(n)

