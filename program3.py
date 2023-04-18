#program ma pobrac liczbe oraz wyswietlic informacje czy uzytkownik zgadl liczbe + powiedziec czy jest za mala czy za duza

szukanaLiczba = 8
zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba: 

    zgadywanaLiczba = int(input("Podaj liczbę:"))

    if (zgadywanaLiczba < szukanaLiczba):
        print("Liczba jest za mała!")
    elif (zgadywanaLiczba > szukanaLiczba):
        print("Liczba jest za duża!")
    else:
        print("Zgadłeś!")
