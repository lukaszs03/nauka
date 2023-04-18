listaLiczb = [1, 2, 3, -2, 0, 7, 124, -25, 5, 6]

def sumazawartosci(listaLiczb):
    return sum([number for number in listaLiczb if number > 0])

print(sumazawartosci(listaLiczb))