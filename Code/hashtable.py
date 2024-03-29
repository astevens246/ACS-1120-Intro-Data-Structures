#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append("{!r}: {!r}".format(key, val))
        return "{" + ", ".join(items) + "}"

    def __repr__(self):
        """Return a string representation of this hash table."""
        return "HashTable({!r})".format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        
        all_keys = [] #creating an empty list to store all the keys
        for bucket in self.buckets: 
            for key, value in bucket.items(): #iterating over the items in the bucket
                all_keys.append(key) #appending the key to the all_keys list
        return all_keys #returning the list of all keys in the hash table

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        
        all_values = [] #creating an empty list to store all the values
        for bucket in self.buckets:# iterating over the buckets 
            for key, value in bucket.items():  # TODO: Collect all values in each bucket
                all_values.append(value)
        return all_values #returning the list of all values in the hash table

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        
        all_items = [] #creating an empty list to store all the items
        for bucket in self.buckets: #iterating over the buckets
            all_items.extend(bucket.items()) #appending the items in the bucket to the all_items list
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        
        # TODO: Loop through all buckets
        all_items = self.items()
        # TODO: Count number of key-value entries in each bucket
        return len(all_items)  # return the total number of key-value entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        
        if key in self.keys(): #checking if the key is in the list of keys
            return True 
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        
        bucket_index = self._bucket_index(key)  #finding the index of the bucket where the key belongs
        bucket = self.buckets[bucket_index] #getting the bucket at the index
        # TODO: Check if key-value entry exists in bucket
        # TODO: Find key-value entry in bucket
        entry = None    #creating a variable to store the entry
        for item in bucket: #iterating over the items in the bucket
            if item[0] == key:
                entry = item
                break
        if entry is not None:   #checking if the entry is not None
            return entry[1] #returning the value associated with the key
        # TODO: If found, return value associated with given key
        if entry is None:
            raise KeyError('Key not found: {}'.format(key))
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        
        bucket_index = self._bucket_index(key)  #finding the index of the bucket where the key belongs
        bucket = self.buckets[bucket_index] #getting the bucket at the index
        entry = None
        for item in bucket: #iterating over the items in the bucket
            if item[0] == key:  
                entry = item
                break
        if entry is not None:   #checking if the entry is not None
            bucket.delete(entry)
        bucket.append((key, value)) # setting the new value for the key
    
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        
        bucket_index = self._bucket_index(key) #finding the index of the bucket where the key belongs
        bucket = self.buckets[bucket_index] #getting the bucket at the index
        entry = None
        for item in bucket: #iterating over the items in the bucket
            if item[0] == key:
                entry = item
                break
        if entry is not None:
            bucket.delete(entry)    #deleting the entry associated with the given key
        else:
            raise KeyError('Key not found: {}'.format(key)) #raising an error if the key is not found
        


def test_hash_table():
    ht = HashTable()
    print("hash table: {}".format(ht))

    print("\nTesting set:")
    for key, value in [("I", 1), ("V", 5), ("X", 10)]:
        print("set({!r}, {!r})".format(key, value))
        ht.set(key, value)
        print("hash table: {}".format(ht))

    print("\nTesting get:")
    for key in ["I", "V", "X"]:
        value = ht.get(key)
        print("get({!r}): {!r}".format(key, value))

    print("contains({!r}): {}".format("X", ht.contains("X")))
    print("length: {}".format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print("\nTesting delete:")
        for key in ["I", "V", "X"]:
            print("delete({!r})".format(key))
            ht.delete(key)
            print("hash table: {}".format(ht))

        print("contains(X): {}".format(ht.contains("X")))
        print("length: {}".format(ht.length()))


if __name__ == "__main__":
    test_hash_table()
