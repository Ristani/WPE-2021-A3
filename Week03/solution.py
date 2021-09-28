class NotEnoughSpaceError(Exception):
    """
    Exception raised when there's not enough space available in a house to add another room.

    Attributes:
        room_size: The size of the room trying to be added.
        available_space: The space available within the house object.
        message (optional): Defines the message to be displayed between the size and space outputs.
    """

    def __init__(self, room_size: int, available_space: int, message="Room size exceeds available space:"):
        self.room_size = room_size
        self.available_space = available_space
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.room_size} -> {self.message} {self.available_space}"
