from objects.house import House


class Mansion(House):
    height = 22
    width = 21
    minimumSpace = 12
    priceIncrease = 0.06
    value = 610000

    def __repr__(self):
        return ("{}".format(self.__class__.__name__))
