from collections import Counter
import typing


class Room:
    """
    This will describe a room in a house.
    """
    def __init__(self, name: str, size: int = 1) -> None:
        self.name, self.size = name, size

    def __str__(self) -> str:
        return f"{self.name}, {self.size}m"


class House:
    """
    This will describe a house, capable of having any number of rooms.
    """
    def __init__(self, available_space: int = 100) -> None:
        self.available_space = available_space
        self.rooms: typing.List[Room] = []

    def __str__(self) -> str:
        return f"{type(self).__name__}:\n" + "\n".join(str(room) for room in self.rooms)

    def add_rooms(self, *new_rooms: Room) -> None:
        """
        Appends supplied objects to the houses list of rooms.
        """
        for room in new_rooms:
            if room.size + self.size() <= self.available_space:
                self.rooms.append(room)
            else:
                raise NotEnoughSpaceError(room.size, self.available_space - self.size())

    def size(self) -> int:
        """
        Returns the sum of the size attribute for all room objects stored in the house.
        """
        return sum(room.size for room in self.rooms)


class SingleFamilyHouse(House):
    def __init__(self, available_space: int = 200) -> None:
        super().__init__(available_space)


class TownHouse(House):
    def __init__(self, available_space: int = 100) -> None:
        super().__init__(available_space)


class Apartment(House):
    def __init__(self, available_space: int = 80) -> None:
        super().__init__(available_space)


class Neighborhood:
    """
    This will describe a neighborhood, capable of having any number of houses.
    """
    total_size = 0

    def __init__(self) -> None:
        self.houses: typing.List[House] = []

    def __str__(self) -> str:
        return f"{type(self).__name__}:\n" + "\n".join(str(house) for house in self.houses)

    def add_houses(self, *new_houses: House) -> None:
        """
        Appends supplied objects to the neighborhoods list of houses.
        """
        for house in new_houses:
            self.houses.append(house)
            Neighborhood.total_size += house.size()

    def size(self) -> int:
        """
        Returns the sum of the size attribute for all house objects stored in the neighborhood.
        """
        return sum(house.size() for house in self.houses)

    def house_types(self) -> typing.Counter[str]:
        return Counter(type(house).__name__ for house in self.houses)


class NotEnoughSpaceError(Exception):
    """
    Exception raised when there's not enough space available in a house to add another room.

    Attributes:
        room_size: The size of the room trying to be added.
        available_space: The space available within the house object.
        message (optional): Defines the message to be displayed between the size and space outputs.
    """

    def __init__(self, room_size: int, available_space: int, message: str = "Room size exceeds space:") -> None:
        self.room_size = room_size
        self.available_space = available_space
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.room_size} -> {self.message} {self.available_space}"
