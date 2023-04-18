"""
    wyrażenie słownikowe
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

nameLengths = {
    name: len(name)
    for name in names
    if name.startswith("A")
}
    
print(nameLengths) 

multipliedNumbers = {
    number: number**number
    for number in range(1, 80)
}

print(multipliedNumbers)

fahrenheit = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
}

print(fahrenheit)