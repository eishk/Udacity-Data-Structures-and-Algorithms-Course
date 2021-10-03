For this problem, I used no new data structures, as all my work was done by
manipulating the given array. For the rearrange_digits function, the space complexity
is O(n) and the time complexity is O(1) as no traversal of the list is done in this
function. However, in merge_sort_array, the time complexity is O(nlogn) because
the problem requires us to reorder the list from largest to smallest. I use the merge
sort algorithm which has a space complexity of O(n), as I create a new array that
will be wholly comprised of the re-ordered list. As for get_expo, the time complexity
is O(n) and the space complexity is O(1) as getting the exponent requires no new space
allocation and depends on size of n.
