class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def search(self, key):
        return self.get(key)

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def resize(self):
        old_table = self.table

        self.size *= 2
        self.table = [[] for _ in range(self.size)]

        for i in old_table:
            for key, value in i:
                self.insert(key, value)

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"[{i}]: {bucket}")
        return "\n".join(result)

hash_table = HashTable(size=5)
value_table = [("apple", 10), ("banana", 20), ("orange", 30), ("grape", 40),("kiwi", 50), ("mango", 60), ("pear", 70), ("peach", 80),("melon", 90), ("berry", 100)]
for key, value in value_table:
    hash_table.insert(key,value)
print(hash_table)

def str_hash(str):
    return sum(ord(char) for char in str)

print(str_hash("abc"))

class HashDict:
    def __init__(self):
        self.data = {}

    def add(self, key):
        hash_value = str_hash(key)
        self.data[key] = hash_value
        return hash_value

    def get(self, key):
        return self.data.get(key, None)


hash_dict = HashDict()


words = ["apple", "orange", "kiwi"]

for word in words:
    hash_value = hash_dict.add(word)

print(hash_dict.data)

new_words = ["apple", "orange", "milk"]
for word in new_words:
    result = hash_dict.get(word)
    if result is not None:
        print(f"Найдено:", word)
    else:
        print(f"Не найдено:", word)