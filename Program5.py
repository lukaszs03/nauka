numbers = (
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if not (number % 5 == 0)
)

for number in numbers:
    print(number)