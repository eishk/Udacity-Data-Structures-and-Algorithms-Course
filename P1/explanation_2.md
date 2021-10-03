For this problem, the main decision I had to make was in terms of what data structure
I would use to hold the files, and I picked a list because the question outlined
the usage of a list. The biggest difficulty in this problem was the recursive aspect,
and I solved it by thinking logically through how the process would work and what would cause the program to fail. As for the complexity of this solution, the time complexity of the find_files_recurse function is O(# of files * # of possible subdirectories), which still comes out to be O(n), as the function looks at each
item returned from os.listdir() a constant number of times. As for the space complexity, the space complexity is O(n) as the space grows linearly only as size grows, and since there are no new data structures being used.
