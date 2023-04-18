def wiad_pow(imie):
    print("Cześć",imie,"witaj w moim programie")
'''
wiad_pow("Arku")
wiad_pow("Wiolu")
wiad_pow("Łukasz")'''

imiona = ["Arku", "Wiolu", "Łukasz"]

for imie in imiona:
    wiad_pow(imie)


a = int(input("Podaj bok A"))
b = int(input("Podaj bok B"))
def pole_prostokata(a, b):
    return(a * b)

print(pole_prostokata(a, b))