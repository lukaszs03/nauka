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

def sumuj_do2(wpis):
    wpis = int(input("Podaj ilość liczb: "))
    return (1 + wpis) / 2 * wpis

def sumuj_do3(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum([wpis for wpis in range(1,wpis)])

def sumuj_do4(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum({wpis for wpis in range(1,wpis)})

def sumuj_do5(wpis):
    wpis = int(input("Podaj ilość liczb: ")) + 1
    return sum((wpis for wpis in range(1,wpis)))

def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

print(function_performance(sumuj_do, 0))
print(function_performance(sumuj_do2, 0))
print(function_performance(sumuj_do3, 0))
print(function_performance(sumuj_do4, 0))
print(function_performance(sumuj_do5, 0))
