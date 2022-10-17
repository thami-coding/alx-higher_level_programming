class Square:
    def __init__(self, size=0):
        self.set_size(size)

    def set_size(self, size):
        if type(size) is not int:

