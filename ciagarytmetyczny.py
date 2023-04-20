import time

def finish_timer(start):
    end = time.perf_counter()
    return end-start

def sumuj_do(liczba):

    suma = 0
    wpis = int(input("Podaj ilość liczb: ")) + 1
    for liczba in range(1, wpis):
        suma = suma + liczba

    return (suma)

start = time.perf_counter()
print(sumuj_do(0))
print(finish_timer(start))

def sumuj_do2(wpis):
    wpis = int(input("Podaj ilość liczb: "))
    return (1 + wpis) / 2 * wpis

start = time.perf_counter()
print(sumuj_do2(0))
print(finish_timer(start))

def sumuj_do3(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum([wpis for wpis in range(1,wpis)])

start = time.perf_counter()
print(sumuj_do3(0))
print(finish_timer(start))

def sumuj_do4(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum({wpis for wpis in range(1,wpis)})

start = time.perf_counter()
print(sumuj_do4(0))
print(finish_timer(start))

def sumuj_do5(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum((wpis for wpis in range(1,wpis)))

start = time.perf_counter()
print(sumuj_do5(0))
print(finish_timer(start))