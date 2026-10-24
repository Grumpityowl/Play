class Relationship:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2
        self.friendship = 0

    def chat(self):
        self.friendship = self.friendship + 1

    def getfriendship(self):
        print(f"Friendship: {self.friendship}")
