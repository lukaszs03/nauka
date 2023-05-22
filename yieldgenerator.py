def generate_even_numbers():
    print("start")
    for element in range(400):
        print("before yield")
        if (element % 2) == 0:
            yield element
            print("after yield")

a = generate_even_numbers()

def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1

print(list(generate_10_numbers()))