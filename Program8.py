from enum import IntEnum

Menu_Wybor = IntEnum('Menu_Wybor', ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek', 'Sobota', 'Niedziela'])

while(True):
    wybor = int(input("""Który dzień tygodnia dziś mamy? ;)
    1. Poniedziałek :(
    2. Wtorek 
    3. Środa
    4. Czwartek
    5. Piątek!1111!!!!
    6. Sobota :D
    7. Niedziela >:(
"""))

    if (wybor == Menu_Wybor.Poniedzialek):
        print("Kawka z ekspresu dla zarządu, dla pana to sypana")
        break
    elif (wybor == Menu_Wybor.Wtorek):
        print("Wtorek czas na worek hehe")
        break
    elif (wybor == Menu_Wybor.Sroda):
        print("Środa dzień loda xd")
        break
    elif (wybor == Menu_Wybor.Czwartek):
        print("Jeśli liczyłeś na jakieś mądre powiedzenie chociaż w czwartek to niestety ale nie u mnie")
        break
    elif (wybor == Menu_Wybor.Piatek):
        print("Piątek piąteczek piątunio")
        break
    elif (wybor == Menu_Wybor.Sobota):
        print("Co mówi programista w sobotę? W sumie to sam nie wiem, jeszcze nim nie jestem")
        break
    elif (wybor == Menu_Wybor.Niedziela):
        print("W głowie się kręci się")
        break