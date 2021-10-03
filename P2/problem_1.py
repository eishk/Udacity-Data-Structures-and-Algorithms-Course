def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return None
    low = 0
    high = number
    found = False
    if number == 1 or number == 0:
        return number
    while not found:
        mid = (low + high) // 2
        if (mid * mid == number):
            return mid
        elif (mid * mid < number):
            if ((mid+1) * (mid+1) > number):
                return mid
            else:
                low = mid
        else:
            high = mid
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# My Test Cases
print(sqrt(None))
# Expected output is None
print(sqrt(67))
# Expected output is 8
print(sqrt(0))
# Expected output is 0
print(sqrt(329476))
# Expected output is 574
