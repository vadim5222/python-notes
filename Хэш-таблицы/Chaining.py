class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def add(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index[i]] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

ht = HashTableChaining(10)
ht.add('ALICE', 90)
ht.add('Bob', 90)
print(ht.get('ALICE'))
print(ht.get('Bob'))