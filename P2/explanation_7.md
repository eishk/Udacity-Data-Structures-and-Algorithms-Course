In this problem, the outlay was to use the basic foundation of problem 5 to
create a pseudo-HTTP Router. To solve the issue presented in the problem, I used a
great deal of recursive techniques and the dictionary data structure to ensure the
tree's growth capabilities. For the RouteTrieNode, the space complexity is essentially
O(n), and the insert function's space complexity is O(1). As for its time complexity,
the creation of the node is O(n) and the insert is O(1). For the RouteTrie, the
initialization function is O(n) for both space and time complexity, while the
insert function in this case has a time complexity of O(n*t), where n is the path and
t is the depth of the trie tree. It has a space complexity of O(1). The find function
for RouteTrieNode is O(n), with it taking linear time to find a path as the path grows.
The Router init function is O(n) in space complexity and O(n) in time complexity.
The add_handler is O(n) with n being length of path in time complexity and O(1) in
space complexity, with the lookup function being O(n) in time complexity and O(1)
in space. As for split path, that is O(n) in time complexity but O(n) in space
complexity as well as it creates a list.
