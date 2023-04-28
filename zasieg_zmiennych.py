def add():
    global c  #zmienna globalna poza definicja c = 1
    c = c + 5 
    return c

c = 1 
print (add())