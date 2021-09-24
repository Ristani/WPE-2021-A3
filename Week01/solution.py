class Room:
    """
    This will describe a room in a house.
    """
    def __init__(self, name: str, size=1):
        self.name, self.size = name, size

    def __str__(self):
        return f"{self.name}, {self.size}m"
