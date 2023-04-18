import pola
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', ['Prostokąt', 'Kwadrat', 'Trójkąt', 'Trapez', 'Koło'])

while(True):
    wybor = int(input(("""Co chcesz zrobić?
    1. Pole prostokąta
    2. Pole kwadratu
    3. Pole trójkąta
    4. Pole trapezu
    5. Pole koła
    6. Zakończ
    """)))

    if (wybor == Menu_Figury.Prostokąt):
        a = float(input("Podaj bok A: "))
        b = float(input("Podaj bok B: ")) 
        print("Wynik to:", pola.pole_prostokata(a, b))
    elif (wybor == Menu_Figury.Kwadrat):
        a = float(input("Podaj bok A: "))
        print("Wynik to:", pola.pole_kwadratu(a))
    elif (wybor == Menu_Figury.Trójkąt):
        a = float(input("Podaj bok A: "))
        h = float(input("Podaj wysokość H: "))
        print("Wynik to:", pola.pole_trojkata(a, h))
    elif (wybor == Menu_Figury.Trapez):
        a = float(input("Podaj bok A: "))
        b = float(input("Podaj bok B: "))
        h = float(input("Podaj wysokość H: "))
        print("Wynik to:", pola.pole_trapezu(a, b, h))
    elif  (wybor == Menu_Figury.Koło):
        r = float(input("Podaj promień R: "))
        print("Wynik to:", pola.pole_kola(r))
    elif (wybor == 6):
        print("PAAAAAAAAAAAAAAAA")
        break
    



