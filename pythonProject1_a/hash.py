class HashTableEntry:

    def __init__(self, key, item):
        self.key = key
        self.item = item

class HashTable:

    #Constructor for hash table initializes table size to 10 buckets.
    #space-time complexity O(N)
    def __init__(self, init_cap=10):
        self.table = []
        #Appends a list to each of the 10 buckets to avoid collisions.
        for i in range(init_cap):
            self.table.append([])

    #Hash algorithm.
    #Determines bucket number based on key input mod table length (In this case, key mod 10).
    #space-time complexity O(1)
    def create_hash(self, key):
        bucket_num = int(key) % len(self.table)
        return bucket_num

    #Adds key/value pair to hash table.
    #space-time complexity O(N)
    def add(self, key, value):
        hash_val = self.create_hash(key)
        value = [key, value]

        if self.table[hash_val] is None:
            self.table[hash_val] = list([value])
            return True
        else:
            for pair in self.table[hash_val]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[hash_val].append(value)
            return True

    #Removes key/value pair from hash table.
    #space-time complexity O(N)
    def remove(self, key):
        hash_val = self.create_hash(key)

        if self.table[hash_val] is None:
            return False
        for i in range(0, len(self.table[hash_val])):
            if self.table[hash_val][i][0] == key:
                self.table[hash_val].pop(i)
                return True
        return False

    #Updates key/value pair with a new value.
    #space-time complexity O(N)
    def update(self, key, value):
        hash_val = self.create_hash(key)

        if self.table[hash_val] is not None:
            for pair in self.table[hash_val]:
                if pair[0] == key:
                    pair[1] = value
        else:
            print('Sorry, that item does not appear to exist.')

    #Returns value associated with key input.
    #space-time complexity O(N)
    def get(self, key):
        hash_val = self.create_hash(key)

        if self.table[hash_val] is not None:
            for pair in self.table[hash_val]:
                if pair[0] == key:
                     return pair[1]

    #Prints hash table
    #space-time complexity O(N)
    def print(self):
        for i in range(len(self.table)):
            print(self.table[i])