import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None

    def add(self, data):
        if data is None:
            break
        if self.head is None:
            self.head = Block(self.gmt(), data, 0)
        else:
            current = self.head
            while(current.next is not None):
                current = current.next
            current.next = Block(self.gmt(),data, current.hash)

    def gmt(self):
        format = '%H:%M %d/%m/%Y'
        return datetime.now().strftime(format)

    def length(self):
        if self.head is None:
            return 0
        else:
            current = self.head
            num = 0
            while current is not None:
                current = current.next
                num += 1
            return num

if __name__ == "__main__":
    chain = Blockchain()
    print(chain.length())
    # Output should be 0
    chain.add(10)
    print(chain.length())
    # Output should be 1
    chain.add(12)
    print(chain.length())
    # Output should be 2
    chain.add(76)
    print(chain.length())
    #Output should be 3
    empty_chain = Blockchain()
    print(empty_chain.length())
    #Output should be 0
    null_chain = Blockchain()
    null_chain.add(None)
    print(null_chain.length())
    # Output should be 0 because no None data in blockchain
    new_ex = Blockchain()
    chain.add(15)
    chain.add(20)
    print(chain.length())
    # Output shuld be 2
