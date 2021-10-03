def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None, None
    sorted_array = merge_sort_array(input_list)
    #correct until here
    num1, num2 = find_max(sorted_array, 0, 0)
    return num1, num2
    pass

def merge_sort_array(list):
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = merge_sort_array(left)
    right = merge_sort_array(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def find_max(array, first , second):
    if (len(array) == 0):
        return first, second
    top = array[0]
    if (len(array) % 2 == 1):
        exponent = get_expo(first)
        first += (top*10**exponent)
    else:
        exponent = get_expo(second)
        second += (top*10**exponent)
    return find_max(array[1:], first, second)

def get_expo(number):
    exponent = 0
    while (number != 0):
        exponent += 1
        number = number // 10
    return exponent

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

# My Test Cases
print(rearrange_digits(None))
# Expected output is None as there is nothing in the given array
print(rearrange_digits([0,0,0]))
# Expected output is [0, 0]
print(rearrange_digits([5,6,9,7,8,3]))
# Expected output is [975, 863]
