from Week03.solution import NotEnoughSpaceError


class House:
    """
    This will describe a house, capable of having any number of rooms.
    """
    def __init__(self, available_space=100):
        self.available_space = available_space
        self.rooms = []

    def __str__(self):
        return f"{type(self).__name__}:\n" + "\n".join(str(room) for room in self.rooms)

    def add_rooms(self, *new_rooms: object):
        """
        Appends supplied objects to the houses list of rooms.
        """
        for room in new_rooms:
            if room.size + sum(room.size for room in self.rooms) <= self.available_space:
                self.rooms.append(room)
            else:
                raise NotEnoughSpaceError(room.size, self.available_space - sum(room.size for room in self.rooms))

    def size(self):
        """
        Returns the sum of the size attribute for all room objects stored in the house.
        """
        return sum(room.size for room in self.rooms)
