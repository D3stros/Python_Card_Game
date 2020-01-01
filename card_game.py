class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


c = Card("A", "Hearts")
c2 = Card("10", "Diamonds")
c3 = Card("K", "Spades")
print(c, c2, c3)
