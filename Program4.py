'''program, ktory:
pozwala dodawac nowe definicje
szukac ich 
usuwac je
uzytkownik!'''


slownik = {}

while(True):
        print("1: Dodaj nową definicję")
        print("2: Znajdź definicję")
        print("3: Usuń definicję")
        print("4: Wyświetł słownik")
        print("5: Zakończ")

        menu = input("Co chcesz zrobic? ")


        if (menu == "1"): 
            key = input("Podaj słowo: ")
            definition = input("Podaj definicję: ")
            slownik[key] = definition
            print("Dodałeś definicję:", key)
        elif (menu == "2"):
            key = input("Czego szukasz? ")
            if key in slownik:
                print(slownik[key])
            else:
                print("Nie znaleziono słowa:", key)
        elif (menu == "3"):
            key = input("Podaj słowo: ")
            if key in slownik:
                del slownik[key]
                print("Pomyślnie usunięto słowo!")
            else:
                print("Nie znaleziono słowa:", key)
        elif (menu == "4"):
            print(slownik)
        elif (menu == "5"):
            print("Do zobaczenia!")
            break
        else:
            print("Nawigujemy liczbami!")