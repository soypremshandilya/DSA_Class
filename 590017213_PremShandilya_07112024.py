class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} already exists at index {index}.")
                return
            
            index = (index + 1) % self.size
            if index == original_index:
                print("Hash table is full!")
                return
        
        self.table[index] = key
        print(f"Inserted key {key} at index {index}.")

    def search(self, key):
        index = self.hash_function(key)

        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            
            index = (index + 1) % self.size
            if index == original_index:
                break
        
        print(f"Key {key} not found.")
        return None

hash_table = HashTable()

hash_table.insert(12)
hash_table.insert(24)
hash_table.insert(36)
hash_table.insert(42)


hash_table.search(24)
hash_table.search(36)
