class P:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__dict__}'


    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)
    
    def __add__(self, other):
        return P(self.name + ' ' + other.name)

class Deck:
    def __init__(self):
        self.__cards = ['A', 'K', 4, 7]

    def __getitem__(self, key):
        return self.__cards[key]

    def __len__(self):
        return len(self.__cards)

    def __add__(self, other):
        return str(self.__cards + other)

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return str(self.__cards)

    