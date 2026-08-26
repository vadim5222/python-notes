#Простая хеш-функция для строк
def simple_hash(key, table_size):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % table_size

table_size = 10
print(simple_hash('Alice', table_size))
print(simple_hash('Bob', table_size))
print(simple_hash('Charlie', table_size))