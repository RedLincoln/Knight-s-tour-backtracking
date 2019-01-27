"""
module that does the implementation of backtracking
uses module ProblemConstraints to discard bad paths
"""
from Stack import Stack
import ProblemConstraints

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1 , -2, -2, -1]
__max_moves__ = 7


class BacktrackingIterator:
    """
    BackTracking iterator class
    """
    init = True

    def __init__(self, n, init_pos):
        """

        :param n: dimension of the board (nxn)
        :param init_pos: initial position in the board
        """
        ProblemConstraints._n = n
        self._n = n
        self.stack_ = Stack(n*n)
        self.moves_stack = Stack(n * n)
        self.init_pos_ = init_pos

    def get_next(self):
        """
        courutine that return one valid combination of positions each time.
        Uses a stack to store combinations and another stack as a counter of possible moves

        :return: a generator of valid combinations of positions
        """
        self.__push__(self.init_pos_, __max_moves__)

        while True:
            if ProblemConstraints.is_valid_combination(tuple(self.stack_.stack_)):
                self.__send_action__(tuple(self.stack_.stack_[-1]), True)
                if self.stack_.top_ == self.stack_.max_size_:
                    yield tuple(self.stack_.stack_)
                    self.__send_action__(self.stack_.top(), False)
                    self.__pop__()
                    if self.stack_.top() is None:
                        return
                    self.__push__(self.stack_.top() + (self._n, self._n), self.moves_stack.pop())
                else:
                    self.__push__(self.stack_.top())
            else:
                while (self.moves_stack.top() + 1) == len(move_x):
                    self.moves_stack.pop()
                    self.__pop__()
                    if self.moves_stack.top() is None:
                        return
                    self.__send_action__(self.stack_.top(), False)
                self.__pop__()
                n_moves = self.moves_stack.pop() + 1
                self.__push__(self.stack_.top(), n_moves)

    def __push__(self, position, index=0):
        """

        :param position: positions to insert in the stack
        :param index: index of moves made
        """
        if not self.init:
            position = (position[0] + move_x[index], position[1] + move_y[index])
        else:
            self.init = False
        self.stack_.push(position)
        self.moves_stack.push(index)

    def __pop__(self):
        """
        pop a element from the stack
        """
        self.stack_.pop()

    def __send_action__(self, position, status):
        """
        send a notification of the state of a cell
        :param position: position of the cell
        :param status: status of the cell
        """
        self._action(position, status, len(self.stack_.stack_))

    def add_action(self, _action):
        """
        add the listener to be used
        :param _action: function to be used
        """
        self._action = _action