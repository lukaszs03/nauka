from enum import IntEnum

Menu_Wybor = IntEnum(['Menu_Wybor', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'])

while(True):
    wybor = int(input("""Który dzień tygodnia dziś mamy? ;)
    1. Poniedziałek :(
    2. Wtorek 
    )"""))