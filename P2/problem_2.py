def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None:
        return -1
    if number is None:
        return -1
    pivot = find_pivot(input_list, 0, len(input_list))
    list1 = input_list[0:pivot+1]
    list2 = input_list[pivot+1:]
    first_result = search_arr(list1, number, 0, len(list1) - 1)
    second_result = search_arr(list2, number, 0, len(list2) - 1)
    if first_result is None and second_result is None:
        return -1
    elif first_result is None:
        return len(list1) + second_result
    else:
        return first_result
    pass

def search_arr(array, target, start_index, end_index):
    if start_index > end_index:
        return None

    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return search_arr(array, target, start_index, mid_index - 1)
    else:
        return search_arr(array, target, mid_index + 1, end_index)


def find_pivot(list, min, max):
    if (max == 0):
        return None
    if (min == len(list)-1):
        return None
    mid = min + max // 2
    if (mid == len(list)-1):
        return mid
    if (list[mid] > list[mid+1]):
        return mid
    if (list[mid] < list[mid-1]):
        return mid-1
    else:
        return find_pivot(list,min,mid) or find_pivot(list,mid,max)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# My Test Cases
print(rotated_array_search(None, 8))
# Prints -1 because 8 cannot be found in None
print(rotated_array_search([7, 8, 9, 1, 2, 3], None))
# Prints -1 because None cannot be found in an array
print(rotated_array_search([7, 8, 9, 3, 4, 5], 5))
# Prints 5 because 5 is the last element in the array at position 5
