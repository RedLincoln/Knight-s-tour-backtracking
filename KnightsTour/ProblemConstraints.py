"""
module that control the logic of a combination being valid
_n: dimension of the board
"""

_n = 5


def is_different_position(array, position):
    """
    check if  position is different from those stored in array
    :param array: array of positions
    :param position: position to be checked
    :return: True if it is different
    """
    for i in range(len(array)):
        if (position[0] == array[i][0]) & (position[1] == array[i][1]):
            return False
    return True


def in_range(position):
    """
    check if the position is inside of the board
    :param position: position to be checked
    :return: True if positions is inside of the board
    """
    return (position[0] >= 0) & (position[0] < _n) & (position[1] >= 0) & (position[1] < _n)


def is_valid_combination(comb_list):
    """
    check if the list of positions is valid
    :param comb_list: list of positions
    :return: True if comb_list is valid
    """
    for i in comb_list:
        if not (in_range(i)):
            return False

    for i in range(1, len(comb_list) + 1):
        if not (is_different_position(comb_list[0:-i], comb_list[-i])):
            return False
    return True
