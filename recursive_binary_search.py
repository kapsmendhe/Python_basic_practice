def recursive_binary_search(list, target):

    if len(list) == 0:
        return False
    else:
        mid = (len(list))/2

    if list[mid] == target:
        return True
    else:
        if list[mid] < target:
            return recursive_binary_search(list[mid + 1:], target)
        else:
            return recursive_binary_search(list[:mid - 1], target)


def verify(index):
    print("Target Found: {index}".format(index=index))


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(number, 4)
verify(result)

result = recursive_binary_search(number, 11)
verify(result)

"""_summary_

    Value --> 1 2 3 4 5 6 7 8 9 10
    Index --> 0 1 2 3 4 5 6 7 8 9

    length = 10

    mid= 10/2=5 (index)
    list[mid]=6 (value)

    list[mid]=target = no
    list[mid]<target = yes

    5+1=6 (index) "Value is 7 from list"
    ------------------------------------
    new list

    Value --> 7 8 9 10
    Index --> 0 1 2 3

    length = 4

    mid= 4/2=2 (index)
    list[mid]=9 (value)

    list[mid]=target = no
    list[mid]<target = yes

    2+1=3 (index) "Value is 10 from list"
    ------------------------------------
    new list

    Value -->10
    Index -->0

    list[mid]=target = Yes

    "Congratulations"

"""
