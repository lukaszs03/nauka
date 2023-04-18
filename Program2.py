#Napisz program, który doda 3 parzyste liczby dodatnie podane przez użytkownika

wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj dodatnią, parzystą liczbę: "))
    if (x % 2 == 0) and (x > 0):
        wynik += x
    else:
        print("Liczba miała być dodatnia/parzysta!")
        continue    
    print("Aktualny wynik dodawania to:", wynik)
    i += 1


