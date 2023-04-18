def sumuj_do(liczba):

    suma = 0
    wpis = int(input("Podaj ilość liczb: ")) + 1
    for liczba in range(1, wpis):
        suma = suma + liczba

    return (suma)

print(sumuj_do(0))

def sumuj_do2(wpis):
    wpis = int(input("Podaj ilość liczb: "))
    return (1 + wpis) / 2 * wpis

print(sumuj_do2(0))

def sumuj_do3(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum([wpis for wpis in range(1,wpis)])

print(sumuj_do3(0))

def sumuj_do4(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum({wpis for wpis in range(1,wpis)})

print(sumuj_do4(0))

def sumuj_do5(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum((wpis for wpis in range(1,wpis)))

print(sumuj_do5(0))