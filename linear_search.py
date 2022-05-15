def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print ("Target found at index ", index)
    else:
        print ("Target not found in a list")


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
    If number is not sorted use below one
    Ex. number.sort()
    It will sort values
"""
result = linear_search(number, 3)
verify(result)

result = linear_search(number, 5)
verify(result)
