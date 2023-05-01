import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

player1deck = []
player2deck = []

random.shuffle(cardList) 

player1deck = cardList[:5]  
player2deck = cardList[5:10]  

print(player1deck)
print(player2deck)
