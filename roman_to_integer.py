""" _Aproch_

    Simply note that a letter subtracts if the letter that follows is "larger". If not, it adds
    Additionally, the last letter must be always added:
"""


def roman_to_integer(roman_num):

    result = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(roman_num) - 1):
        if roman_dict[roman_num[i]] < roman_dict[roman_num[i + 1]]:
            result -= roman_dict[roman_num[i]]
        else:
            result += roman_dict[roman_num[i]]
    result += roman_dict[roman_num[-1]]
    return result


print(roman_to_integer("IV"))
