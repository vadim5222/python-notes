class HashTableOpenAdressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def add(self, key, value):
        index = self.hash(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

ht = HashTableOpenAdressing(10)
ht.add('Alice', 90)
ht.add('Bob', 85)
print(ht.get('Bob'))