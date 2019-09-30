import hashlib

class HashTable:
    def __init__(self):
        self.table = [ [] for i in range(50) ]
    
    def add(self, key, val):
        idx = self.hash(key)
        self.table[idx].append(val)

    def get(self, key):
        # returns the value
        idx = self.hash(key)
        return self.table[idx]

    def hash(self, key):
        # returns an index
        # hash_object = hashlib.md5(key.encode()) # pass into the hashing algorithm the raw byte sequence
        # hex_digest = hash_object.hexdigest() # get the hex string representing the hash
        # decimal_digest = int(hex_digest, 16) # convert to base 10
        # print(hex_digest)
        # print(decimal_digest)


        # Todo:
        # Implement your own hash function!
        char_sum = 0
        for i in range(len(key)):
            char_sum += ord(key[i]) * i
        num = int(((char_sum * 91) / 7) * 29 / 3)
        return num % len(self.table) # return the index

    def print(self):
        unused = 0
        collisions = 0
        total_items = 0

        for bucket in self.table:
            if len(bucket) == 0:
                unused += 1
            elif len(bucket) > 1:
                collisions += len(bucket) - 1
            total_items += len(bucket)

        load_factor = (len(self.table) - unused) / len(self.table) * 100

        print(f'The current load factor is: {load_factor}%\nThere are {collisions} collision(s) for {total_items} items')


# Bonus: Look into Hash table dynamic resizing (key term: load factor)
# Bonus: Look into Hash table collision technique: Open Addressing

phonebook = HashTable()
phonebook.add('206-123-4444', 'Henry H')
phonebook.add('206-123-3321', 'Jane Doe')
phonebook.add('998-123-8848', 'Sully')
phonebook.add('206-123-1234', 'Mike Wazowski')
phonebook.add('422-322-1235', 'Randall Boggs')
phonebook.add('000-123-1111', 'Yeti')

phonebook.add('123-456-7890', 'A')
phonebook.add('234-456-7890', 'B')
phonebook.add('123-999-7890', 'C')
phonebook.add('123-456-1234', 'D')
phonebook.add('444-393-3393', 'E')
phonebook.add('448-450-7890', 'F')
phonebook.add('123-888-7890', 'G')
phonebook.add('998-420-3232', 'H')
phonebook.add('444-891-6789', 'I')
phonebook.add('124-124-4444', 'J')
phonebook.add('125-125-9995', 'K')
phonebook.add('000-842-9999', 'L')
phonebook.add('789-842-9999', 'M')
phonebook.add('123-932-9999', 'N')
phonebook.add('444-939-5399', 'O')
phonebook.add('654-949-5399', 'P')
phonebook.add('324-259-5399', 'Q')
phonebook.add('902-299-5399', 'R')
phonebook.add('533-299-5399', 'S')
phonebook.add('790-209-5399', 'T')
phonebook.add('783-292-5399', 'U')
phonebook.add('909-283-5399', 'V')
phonebook.add('321-292-5399', 'W')
phonebook.add('322-292-5399', 'X')
phonebook.add('454-292-5399', 'Y')
phonebook.add('677-292-5399', 'Z')

phonebook.print()
# print(phonebook.table)

print(phonebook.table)