class Room:
    """
    This will describe a room in a house.
    """
    def __init__(self, name: str, size: int):
        """
        Initialise room attributes.
        """
        self.name = name
        self.size = size

    def __str__(self):
        """
        Define the string representation of the object.
        """
        return f"{self.name}, {self.size}m"


class House:
    """
    This will describe a house, capable of having any number of rooms.
    """
    def __init__(self):
        """
        Initialize house attributes.
        """
        self.rooms = []

    def __str__(self):
        """
        Defines the string representation of the house object.
        """
        return "House:\n{}".format("\n".join(str(room) for room in self.rooms))

    def add_rooms(self, *args):
        """
        Appends supplied arguments to the object rooms list.
        """
        self.rooms += args

    def size(self):
        """
        Returns the sum of the size attribute for all room objects stored in the house.
        """
        return sum(room.size for room in self.rooms)
