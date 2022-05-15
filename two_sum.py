"""_Que_
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
    ***Using two-pointers***

    Just define two pointers one from start and the other from the end
    In a while loop check if sum of both the pointers is equal to the target
    if yes, return the indices
    else decrease the end pointer by 1.
    if l == r that means we didnot find the combination with start as a fixed point.
    So, increase start pointer by 1 and end pointer goes to original position. and repeat the process.
"""


def two_sum(list, target):
    first_pointer = 0
    last_pointer = len(list) - 1

    while (first_pointer <= last_pointer):
        if list[first_pointer] + list[last_pointer] == target:
            return [first_pointer, last_pointer]
        else:
            last_pointer -= 1

        if first_pointer == last_pointer:
            first_pointer += 1
            last_pointer = len(list) - 1
    return "Sum target not found"


number = [2, 7, 11, 15]
print(two_sum(number, 14))


"""
    ***Using Hash-table**

    create a dictionary with the element as the key and it's index as a value
    if we have repeated elements in the array store that element as a list in value to that key
    example: [3, 2, 1, 2, 5]; dictionary will be created as {3:[0], 2:[1, 3], 1:[2], 5[4]}
    now for i in dictionary, if target - i is != i and target - i in dictionary,
    which means target is not equal to sum of same number
    for example target = 5; i = 3; target - i = 2 which is in dictionary then return indices of 5 and 2
    another case : target = 4; i = 2; target - i = 2; and the key's length is > 1; then return the value 1 and value 2.

    def two_sum(lst, target):
    dictu = {}
    import pdb;pdb.set_trace()
    for i in range(len(lst)):
        if lst[i] not in dictu:
            dictu[lst[i]] = [i]
        else:
            dictu[lst[i]].append(i)
    for i in dictu:
        if i != target-i and target - i in dictu:
            return [dictu[i][0], dictu[target-i][0]]
        elif i == target - i and len(dictu[i]) > 1:
            return [dictu[i][0], dictu[i][1]]
"""
