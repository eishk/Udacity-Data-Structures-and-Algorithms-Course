For this problem, I implemented the trie data structure, and did that by making the
TrieNodes hold only whether it was a word and a dictionary to continue the chain.
The space complexity of a dictionary is O(n), and the inserting function for
TrieNodes, since it is basely a dictionary, is O(1). The suffixes function in
TrieNode has a space complexity of O(n) as it uses a list data structure, and its
time complexity is O(n*t), with n being the suffix given and t the level of nodes in
the Trie that the suffix is in. As for the Trie, the Trie is composed of all
TrieNodes, and it's insert function is based on O(n) as it
requires iteration over the given word. As for the find function, time complexity is
O(n) as it requires iteration over the given prefix as well. Space complexities for
both functions is O(1) as they are accessing previously made data structures.
