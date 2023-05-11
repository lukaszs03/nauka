try:
    file = open("sample.txt", "w")
    file.write("test\n")
    file.write("test")

finally:
    file.close()

with open("sample2.txt", "w") as file:
    file.write("test\n")
    file.write("test")
    
with open("oceans.txt", "r", encoding="UTF-8") as file:
    oceans = file.read().splitlines()
    oceans2 = file.readline() #jak masz readline to wskazuje tylko jeden z listy, np 2 = Spokojny
    oceans3 = file.readlines() #koncowka s printuje wszystko jako lista + zachowuje \n
    print(oceans)
    #print(oceans2)
    #print(oceans3)

print("---------")

with open("oceans.txt", "r", encoding="UTF-8") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell()) #+ 2 bo \n
    file.seek(0)
    print(file.tell())
    print(file.readline())
    print(file.tell())

print("---------")

with open("oceans.txt", "a", encoding="UTF-8") as file:
    file.write("\nTest")

print("---------")

with open("oceans.txt", "a+", encoding="UTF-8") as file:
    file.write("\nTest2")
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("\nTest3")