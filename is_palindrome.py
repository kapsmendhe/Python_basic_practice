def is_palindrome(x):
    """
    Convert Integer into string and then reverse
    # y = str(x)
    # return y == y[::-1]
    """
    reverse = 0
    number = x
    while(number > 0):
        reminder = number % 10
        reverse = (reverse*10) + reminder
        number = number//10
    if reverse == x:
        return True
    return False
