import math

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a * a

def pole_trojkata(a, h):
    return a * h / 2

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

def pole_kola(r):
    return math.pi * r ** 2  

while(True):
    print("1: Obliczyć pole prostokąta")
    print("2: Obliczyć pole kwadratu")
    print("3: Obliczyć pole trójkąta")
    print("4: Obliczyć pole trapezu")
    print("5: Obliczyć pole koła")
    print("6: Zakończ")
    menu = float(input("Wybierz co chcesz zrobić nawigując numerami: "))
    if menu == 1:
        a = float(input("Podaj bok A: "))
        b = float(input("Podaj bok B: "))
        print("Wynik to:", pole_prostokata(a, b))
    elif menu == 2:
        a = float(input("Podaj bok A: "))
        print("Wynik to:", pole_kwadratu(a))
    elif menu == 3:
        a = float(input("Podaj bok A: "))
        h = float(input("Podaj wysokość H: "))
        print("Wynik to:", pole_trojkata(a, h))
    elif menu == 4:
        a = float(input("Podaj bok A: "))
        b = float(input("Podaj bok B: "))
        h = float(input("Podaj wysokość H: "))
        print("Wynik to:", pole_trapezu(a, b, h))
    elif menu == 5:
        r = float(input("Podaj promień R: "))
        print("Wynik to:", pole_kola(r))
    elif menu == 6:
        print("PAAAAAAAAAAAAAAAA")
        break
    



