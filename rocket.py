# trzeba dokonczyc silniki ok spoko gagri
from random import randint


class Rocket:

    def __init__(self):
        self.altitude = 0

    def move_up(self):
        self.altitude += 1


rockets = [Rocket() for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, 4)
    rockets[rocketIndexToMove].move_up()

for rocket in rockets:
    print(rocket.altitude)
