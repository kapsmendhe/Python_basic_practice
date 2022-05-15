def binary_search(list, target):
    first = 0
    last = len(list)

    while(first <= last):
        mid_point = (first + last)/2

        if list[mid_point] == target:
            return mid_point
        elif mid_point < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: {index}".format(index=index))
    else:
        print("Target Not found in a list")


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
    If number is not sorted use below one
    Ex. number.sort()
    It will sort values
"""
result = binary_search(number, 6)
verify(result)

result = binary_search(number, 10)
verify(result)
