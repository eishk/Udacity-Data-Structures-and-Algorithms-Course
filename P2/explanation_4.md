For the sort_012 function, I decided to use no extra space and keep the space
complexity at O(1) using in-array sorting. Basically, I sort in place. If place was 0,
keep it there and move marker forward. If place was 2, switch that with the back
element and recheck. And if it was 1, just move on the place. The time complexity
for this is O(n), as it takes one traversal of the array.
