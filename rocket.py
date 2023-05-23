# trzeba dokonczyc silniki ok spoko gagri
from random import randint


class Rocket:
    
    def __init__(self, speed=1):
        self.altitude = 0

        self.speed = speed

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is on height: " + str(self.altitude) + ", and her speed is: " + str(self.speed)

rockets = [Rocket(randint(1, 6)) for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, len(rockets) - 1)
    rockets[rocketIndexToMove].move_up()


for rocket in rockets:
    print(rocket)
