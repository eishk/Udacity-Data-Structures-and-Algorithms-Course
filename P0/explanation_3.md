This was probably the most difficult of the parts for me, as choosing the data
structure was a long and tedious process, and on top of that implementing the
data structure was extremely difficult. I chose to use a min heap implementation
after doing research on it, because it was the most efficient way of creating a
priority queue. I then used a dictionary to hold all the huffman encoded paths
from the tree, as it allowed for the fastest retrieval time. The complexity of
this algorithm is O(nlogn), as it takes O(logn) time for the minheap to determine
the highest priority queue to be popped out and then for the next weight to be
inserted, and there are O(n) iterations for each item. 
