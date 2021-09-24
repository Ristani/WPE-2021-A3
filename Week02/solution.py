class House:
    """
    This will describe a house, capable of having any number of rooms.
    """
    def __init__(self):
        self.rooms = []

    def __str__(self):
        return f"{type(self).__name__}:\n" + "\n".join(str(room) for room in self.rooms)

    def add_rooms(self, *new_rooms: object):
        """
        Appends supplied objects to the houses list of rooms.
        """
        self.rooms += new_rooms

    def size(self):
        """
        Returns the sum of the size attribute for all room objects stored in the house.
        """
        return sum(room.size for room in self.rooms)
