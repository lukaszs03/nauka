def infinite_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number

generatedNumbers = []
numberGenerator = infinite_generator()

for k in range(20):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)
