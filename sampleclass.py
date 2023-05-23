class User:

    def __init__(self, age, name):
        print("bla bla bla")

        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, "wiek: ", self.age, self.name)

user1 = User(30, "Łukasz")
user2 = User(40, "Arek")

user1.print_age("dodatkowy tekst")
user2.print_age("dodatkowy tekst x")

print(user1.ageInFuture)