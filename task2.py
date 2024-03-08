class ones_threes_nines:

    def __init__(self, n):
        self.ones = n
        self.threes = n // 3
        self.nines = n // 9

n1 = ones_threes_nines(5)
print(n1.nines)
print(n1.ones)
print(n1.threes)