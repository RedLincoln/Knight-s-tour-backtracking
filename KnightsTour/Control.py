"""
Control the program
"""
from BacktrackingIteratorKnightTour import BacktrackingIterator
import GUI
import time
import Console_arguments_handler

dimension = 5
frequency = 1
init_position = (0, 0)


def get_arguments():
    """
    use the module Console_arguments_handler to check if any option was used
    """
    global frequency, dimension, init_position
    arguments = Console_arguments_handler.arguments
    if 'frequency' in arguments:
        frequency = arguments['frequency']
    if 'dimension' in arguments:
        dimension = arguments['dimension']
    if 'init_position' in arguments:
        init_position = arguments['init_position']


def new_comb(positions, status, text):
    """
    used as listener each time the model change the status of a valid combination
    :param positions: position in the board
    :param status: selected (True) of not selected
    :param text: text to be displayed if is selected
    """
    root.set_cell_status(positions[0], positions[1], status, text)
    root.update()
    time.sleep(frequency)


Console_arguments_handler.check_arguments()
get_arguments()

root = GUI.GUI(dimension=dimension)

root.update()

knight_problem = BacktrackingIterator(dimension, init_position)
knight_problem.add_action(lambda comb, status, text: new_comb(comb, status, text))
iterator = knight_problem.get_next()


for i in iterator:
    print(i)
    time.sleep(7)

print("out of the  loop")


