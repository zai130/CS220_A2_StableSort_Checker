class IndexedInteger:
    def __init__(self, value, index):
        self.value = int(value)
        self.index = index

    def __int__(self):
        return int(self.value)

    def __add__(self, other):
        return self.value + int(other)

    def __sub__(self, other):
        self.value - int(other)

    def __eq__(self, other):
        return self.value == int(other)

    def __lt__(self, other):
        return self.value < int(other)

    def __le__(self, other):
        return self.value <= int(other)

    def __gt__(self, other):
        return self.value > int(other)

    def __ge__(self, other):
        return self.value >= int(other)

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)