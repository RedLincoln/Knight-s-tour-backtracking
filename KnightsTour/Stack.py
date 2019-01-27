class Stack:
    """Stack to store elements"""

    def __init__(self, max_size):
        """

        :param max_size: set a maxsize of the stack
        """
        self.max_size_ = max_size - 1
        self.top_ = -1
        self.stack_ = []

    def top(self):
        """

        :return: return the element in the top of the stack
        """
        if self.top_ > -1:
            return self.stack_[self.top_]

    def push(self, element):
        """
        insert a element in the stack
        :param element: element to insert
        """
        if len(self.stack_) <= self.max_size_:
            self.top_ += 1
            self.stack_.append(element)

    def pop(self):
        """
        remove the top element and returns it
        :return: the top element of the stack
        """
        if self.top_ > -1:
            self.top_ -= 1
            return self.stack_.pop()



    
    
