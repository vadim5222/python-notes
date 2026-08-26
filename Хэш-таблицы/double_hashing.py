class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return sum(ord(c) for c in key) % self.size

    def hash2(self, key):
        return 7 - (sum(ord(c) for c in key) % 7)

    def add(self, key, value):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            i += 1
            index = (self.hash1(key) + i * step) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (self.hash1(key) + i * step) % self.size
        return None

ht = HashTableDoubleHashing(10)
ht.add('Alice', 90)
ht.add('Bob', 85)
ht.add('Charlie', 92)
print(ht.get('Alice   '))

