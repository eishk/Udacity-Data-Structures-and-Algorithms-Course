def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None
    max = float('-inf')
    min = float('inf')
    for int in ints:
        if int > max:
            max = int
        if int < min:
            min = int
    return (min, max)
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# My Test Cases
zero_list = [0 for i in range(0, 10)]
print("Pass" if ((0, 0) == get_min_max(zero_list)) else "Fail")
# Should print pass as a list of all 0s has a min and max of 0
none_list = None
print("Pass" if (None == get_min_max(none_list)) else "Fail")
# Should print pass as a Nonetype shoyld return None
large_list = [i for i in range(-1000, 2001)]
print("Pass" if ((-1000, 2000) == get_min_max(large_list)) else "Fail")
# Should print pass as -1000 is min and 2000 is max
