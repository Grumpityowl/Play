import time
import random

class Fish:
    def __init__(self, name, price, rarity):
        self.name = name
        self.price = price
        self.rarity = rarity

carp = Fish("Carp", 10, 50)
bass = Fish("Bass", 20, 30)
salmon = Fish("Salmon", 50, 20)
harp = Fish("Harp", 200, 1)

def fish(person):
    print(f"{person.name} went fishing!")

    time_waited = random.randint(2, 10)
    print(f"You wait {time_waited} seconds...")
    time.sleep(time_waited)
    fish = random.choices(
    [carp, bass, salmon],
    weights=[carp.rarity, bass.rarity, salmon.rarity]
        )[0]
    person.money = person.money + fish.price  
    input("Do you want to sell your fish? ")  #rhetorical question. I'm not letting you not.
    print(f"{person.name}'s finances: ${person.money}")