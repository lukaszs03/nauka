import math

type = str(input("Wybierz działanie + - dodawanie, - - odejmowanie, * mnożenie, / dzielenie, % modulo, ** potęgowanie, sqrt pierwiastkowanie: "))

a = int(input("Podaj pierwszą liczbę: ")) 
b = int(input("Podaj drugą liczbę: "))

if (type == '+'):
    print(a + b)
elif (type == '-'):
    print(a - b)
elif (type == '*'):
    print(a * b)
elif (type == '/'):
    if (b == 0):
        print("Nie dziel przez 0 debilu")
    else:
        print(a / b)
elif (type == '%'):
    print(a % b)
elif (type == '**'):
    print(a ** b)
elif (type == 'sqrt'):
    print(math.sqrt(a))
    print(math.sqrt(b))