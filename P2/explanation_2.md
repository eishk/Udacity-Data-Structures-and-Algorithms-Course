For this problem, my approach was to use binary search to find the pivot point
around which the sorted array went from highest to lowest, then split the array
into two arrays at that point, and search those arrays for the number. To do so,
it required the rotated_array_search to create new lists to hold parts of the main
list, but no other new auxiliary data structures, which made space complexity
O(n). As for the searching aspect, this was binary search so the time complexity was
O(nlogn). Overall, the solution takes O(n) space and O(nlogn) time.
