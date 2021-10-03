class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.main_dict = {}
        self.key_dict = {}
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if (self.size == 0 or key is None):
            return -1
        if (key in self.main_dict):
            self.key_dict[key] = self.key_dict[key] + 1
            return self.main_dict[key]
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.main_dict:
            if (self.size == self.capacity):
                least_used_element = min(self.key_dict,
                          key=lambda k: self.key_dict[k])
                self.main_dict.pop(least_used_element)
                self.key_dict.pop(least_used_element)
                self.size -= 1
            self.size += 1
            self.key_dict[key] = 0
            self.main_dict[key] = value
        pass


def main():
    #Given test cases
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))

    #My Own Test Cases
    my_cache = LRU_Cache(3)
    print(my_cache.get(5))
    # Output should be -1
    my_cache.set(1, 3)
    my_cache.set(3, 5)
    my_cache.set(4, 6)
    print(my_cache.get(4))
    # Output should be 6
    print(my_cache.get(3))
    # Output should be 5
    my_cache.set(2, 8)
    print(my_cache.get(1))
    # Output should be -1 since 1 was least used and capacity is 3, so 2 takes
    # its place
    print(my_cache.get(None))
    # Output should be -1 since null value is not found in cache.
    null_cache = LRU_Cache(0)
    print(my_cache.get(1))
    # Output should be -1 since null value is not found in cache.




if __name__ == '__main__':
    main()
