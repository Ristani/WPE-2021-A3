class Neighborhood:
    """
    This will describe a neighborhood, capable of having any number of houses.
    """
    total_size = 0

    def __init__(self):
        self.houses = []

    def __str__(self):
        return f"{type(self).__name__}:\n" + "\n".join(str(house) for house in self.houses)

    def add_houses(self, *new_houses: object):
        """
        Appends supplied objects to the neighborhoods list of houses.
        """
        for house in new_houses:
            self.houses.append(house)
            Neighborhood.total_size += house.size()

    def size(self):
        """
        Returns the sum of the size attribute for all house objects stored in the neighborhood.
        """
        return sum(house.size() for house in self.houses)
