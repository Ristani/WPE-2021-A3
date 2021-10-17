from Week02.solution import House


class SingleFamilyHouse(House):
    def __init__(self, available_space=200):
        super().__init__(available_space)


class TownHouse(House):
    def __init__(self, available_space=100):
        super().__init__(available_space)


class Apartment(House):
    def __init__(self, available_space=80):
        super().__init__(available_space)
