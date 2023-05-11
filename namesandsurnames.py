
namesandsurnames = []

with open("namesandsurnames.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesandsurnames.append(tuple(line.replace("\n", "").split(" ")))

with open("names.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurnames:
        file.write(item[0] + "\n")

with open("surnames.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("-\n")

#print(namesandsurnames)