import sys
import heapq


class Node:

    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return other.frequency > self.frequency

    def __str__(self):
        return str(self.char)+" "+str(self.frequency)

def huffman_encoding(data):
    if (len(data) == 0):
        return "", None
    tree_dict = dict()
    for i in range(len(data)):
        char = data[i]
        if char in tree_dict:
            tree_dict[char] += 1
        else:
            tree_dict[char] = 1
    queue = sorted(zip(tree_dict.values(), tree_dict.keys()))
    for i in range(len(queue)):
        value = queue[i][1]
        freq = queue[i][0]
        queue[i] = Node(value, freq)
    heapq.heapify(queue)
    tree = None
    if (len(queue) is 1):
        first_node = heapq.heappop(queue)
        new_node = Node(None, first_node.frequency)
        new_node.left = first_node
        heapq.heappush(queue, new_node)
    else:
        while(len(queue) is not 1):
            first_node = heapq.heappop(queue)
            second_node = heapq.heappop(queue)
            new_node = Node(None, first_node.frequency + second_node.frequency)
            new_node.left = first_node
            new_node.right = second_node
            heapq.heappush(queue, new_node)
    tree = queue
    encoded_dict = create_table(tree)
    encoded = ""
    for item in data:
        encoded += encoded_dict[item]
    return encoded, tree
    pass

def create_table(tree):
    code = {}
    def getCode(node, enc = ""):
        if node is None:
            return
        if node.left is None and node.right is None:
            code[node.char] = enc
        getCode(node.left, enc + "0")
        getCode(node.right, enc + "1")
    getCode(tree[0])
    return code

def huffman_decoding(data,tree):
    if data is None or tree is None:
        return ""
    string = ""
    place = tree[0]
    for part in data:
        if part is "0":
            place = place.left
        elif part is "1":
            place = place.right
        if place.left is None and place.right is None:
            string += place.char
            place = tree[0]
    return string


if __name__ == "__main__":
    codes = {}
    #Given example
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #First Test Case
    nothing = ""
    print ("The content of the data is: {}\n".format(nothing))
    #Output should be ""

    encoded_data, tree = huffman_encoding(nothing)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #Output should be ""

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #Output should be ""

    #Second Test Case
    long_statement = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.The bee, of course, flies anyway"

    print ("The size of the data is: {}\n".format(sys.getsizeof(long_statement)))
    # Output should be 233
    print ("The content of the data is: {}\n".format(long_statement))
    # Output is the long_statement string

    encoded_data, tree = huffman_encoding(long_statement)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output should be 128
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output should be 111001001010011010011111011001110110100110111110000010111111001001100010000011100111110111111011111101100100010010111101010011111101000100111101010010010011011010011111101110101000101110101111000110011000001000101001101111110001111100101110001001000110111001100000101101011111110100010001110110001101110000100101101100011000010111111001101010000111011101000011100110101101010001111010011011111000010100100101100110000101111111111000101111001011001100010000010111111001110001100101100010010110101001101010011011001000010010111011100011000001101111111101101110001111110101101000101110101111000011100001100111110100011011111011111010011101011101011110000011011100110010101000111111010001010011111101000011000101110010101000110101000010011000101001001110110111001111100101110

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output should be 233
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Output is the long_statement string

    #Third Test Case
    final = "This is my final test case."

    print ("The size of the data is: {}\n".format(sys.getsizeof(final)))
    # Output should be 76
    print ("The content of the data is: {}\n".format(final))
    # Output is the final string

    encoded_data, tree = huffman_encoding(final)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output should be 40
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output should be 101011010001010000010100000111011010001101101001101111101110011001110100110000011111111100111010110
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output should be 76
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Output is the final string


    #Fourth Test Case
    final = "BBBBBBBBB"

    print ("The size of the data is: {}\n".format(sys.getsizeof(final)))
    # Output should be 58
    print ("The content of the data is: {}\n".format(final))
    # Output is the final string

    encoded_data, tree = huffman_encoding(final)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output should be 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output should be 000000000
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output should be 58
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Output is the final string
