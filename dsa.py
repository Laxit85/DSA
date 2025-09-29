
# set method og ht with collision handling
>>>>>>> a40a7dc (Updated dsa.py with new code)
class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.data_map = [None] * self.size

    def _hash(self, key):
        """Hash function to compute the index for a given key."""
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def print_table(self):
        """Print the contents of the hash table."""
        for i, item in enumerate(self.data_map):
            if item is not None:
                print(f"Index {i}: {item}")

    def set_item(self, key, value):
        """Set the item of the dictionary."""
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
#get method of ht with collision handling

    def get_item(self, key):
        """Get the item from the dictionary."""
        index = self._hash(key)
        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None
    

my_hash_table.set_item('name', 'Alice')
my_hash_table.set_item('age', 30)
my_hash_table.set_item('city', 'New York')

my_hash_table.print_table()
print(my_hash_table.get_item('name'))  # Output: Alice

