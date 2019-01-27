"""
module to get the console arguments
it is stored in arguments as a dictionary
options:
-d dimension
-f frequency
-i initial position
"""
import sys


arguments = {}


class LiteralArgumentRequired(Exception):
    pass


class IncompatibleTypes(Exception):
    pass


class LessThanZeroException(Exception):
    pass


def check_arguments():
    """
    check if any option was passed as argument
    """
    if '-f' in sys.argv:
        index = sys.argv.index('-f') + 1
        __check_argument_literal(index, float, '-f')
        arguments.setdefault('frequency', float(sys.argv[index]))
    if '-d' in sys.argv:
        index = sys.argv.index('-d') + 1
        __check_argument_literal(index, int, '-d')
        arguments.setdefault('dimension', int(sys.argv[index]))
    if '-i' in sys.argv:
        first_index = sys.argv.index('-i') + 1
        __check_argument_literal(first_index, int, '-i')
        second_index = sys.argv.index('-i') + 2
        __check_argument_literal(second_index, int, '-i')
        arguments.setdefault('init_position', tuple(map(int, [sys.argv[first_index], sys.argv[second_index]])))


def __check_argument_literal(index, expected_type, option):
    """
    check possible exceptions

    :param index: check out of bound index
    :param expected_type: for type conversion
    :param option: used to know indicate where is the error
    """
    try:
        if index not in range(len(sys.argv)):
            raise LiteralArgumentRequired('Argument required after {} option'.format(option))
        if expected_type(sys.argv[index]) <= 0:
            raise LessThanZeroException('argument greater than 0 expected after {} option'.format(option))
    except ValueError:
        print('{} type expected after {} option'.format(expected_type, option))
    except Exception:
        exc_type, message, _ = sys.exc_info()
        print(exc_type, message)
    else:
        return None
    print('[python] Control.py [-d dimension| -f refresh_frequency | -i x_position y_position]')
    exit(1)