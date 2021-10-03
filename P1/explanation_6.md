The main decision I made here was in terms of implementing the union and intersection,
and I chose to do those differently for each situation. For the intersection,
I knew intersection was only when two lists had the same numbers, so I had to parse
through both list and then create a new list that was only appended to if
it was in both lists and not already in the new list. The union code was much
easier as I used the data structure of the set to ensure no duplicates were added
and all unique #s were added. For the time complexity of the
union code, the time complexity is O(n), as the union method requires the traversal of both lists given. This is to ensure that all union data points are found. In terms of space complexity, the complexity is at worst O(n) as a new LinkedList is created and a new set is created. For the intersection method, the time complexity is O(n^2), as to populate the list with the data takes O(n), and then it requires a double nested loop to append to the intersection list. The space complexity is O(n) as the list at worst is O(n) time and same for the final linked list.
