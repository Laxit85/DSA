
#SET method in HT
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

my_hash_table = HashTable()

my_hash_table.set_item('name', 'Alice')
my_hash_table.set_item('age', 30)
my_hash_table.set_item('city', 'New York')

my_hash_table.print_table()

