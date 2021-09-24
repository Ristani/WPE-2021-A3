class Room:
    """
    This will describe a room in a house.
    """
    def __init__(self, name: str, size: int):
        """
        Initialise room attributes.
        """
        self.name, self.size = name, size

    def __str__(self):
        """
        Define the string representation of the object.
        """
        return f"{self.name}, {self.size}m"
