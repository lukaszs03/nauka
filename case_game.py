import random


chests = ["green", "orange", "purple", "gold", "nothing"]

def menu(): 
    return int(input("Aby pójść prosto wciśnij 1, aby pójść w lewo wciśnij 2, a w prawo 3!: "))

def prize():
    result = random.choices(chests, [0.30, 0.20, 0.10, 0.05, 0.25], k = 1)
    if result[0] == "green":
        print("Brawo! Znalazłeś zieloną skrzynię, a w niej 1000 golda!")
        return 1000
    if result[0] == "orange":
        print("Nieźle! Znalazłeś pomarańczową skrzynię, a w niej 4000 golda!")
        return 4000
    if result[0] == "purple":
        print("Extra! Znalazłeś fioletową skrzynię, a w niej 9000 golda!")
        return 9000
    if result[0] == "gold":
        print("WOOW! Znalazłeś ZŁOTĄ skrzynię, a w niej 16000 golda!")
        return 16000
    if result[0] == "nothing":
        print("Nic nie znalazłeś! Co za pech!")
        return 0
print("Uwaga! Wpadłeś do komnaty pełnej skarbów i masz okazję się wzbogacić!")


x = 0
balance = 0

while x < 5:
    choice = menu()
    if choice in [1, 2, 3]:
        balance += prize()
        print("Aktualnie w sakwie masz:", balance, '\n')
        x += 1

    if x == 5: 
        print("Udało ci się znaleźć wyjście, pora na jakąś kurtyzanę hehe")



#from collections import Counter
#print(Counter(random.choices(chests, [0.75, 0.20, 0.04, 0.01], k = 1)))