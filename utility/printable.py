class Printable:
    """A base class that implements printing functionality for the class."""

    def __repr__(self):
        return str(self.__dict__)
