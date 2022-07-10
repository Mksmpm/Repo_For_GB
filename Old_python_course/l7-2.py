from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    @abstractmethod
    def cloth_consumed(self):
        pass

    def __add__(self, other):
        return self.cloth_consumed + other.cloth_consumed


class Coat(Clothes):

    @property
    def cloth_consumed(self):
        return round(self.parameter / 6.5) + 0.5


class Suit(Clothes):

    @property
    def cloth_consumed(self):
        return 2 * self.parameter + 0.3


some_coat = Coat(120)
some_suit = Suit(140)

print(f"cloth consumed for coat and suit: {some_suit + some_coat}")
