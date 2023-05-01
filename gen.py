import random
"""
def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

choose_random_numbers(6, 49)
"""
random_numbers = []
numbers = 10

def choose_random_numbers2(amount, total_amount):
    chosen_numbers = set()
    while len(chosen_numbers) < amount:
        chosen_numbers.add(random.randint(1, total_amount))
    return chosen_numbers

for i in range(numbers):
    random_numbers.append(choose_random_numbers2(3, 100))
print(random_numbers)
