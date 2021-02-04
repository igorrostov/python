class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return round(self.width / 6.5 + 0.5, 2)

    def get_square_jacket(self):
        return round(self.height * 2 + 0.3, 2)

    @property
    def get_square_full(self):
        return str(f'Общая площадь ткани \n'
                   f'{round(self.width / 6.5 + 0.5, 2) + round(self.height * 2 + 0.3, 2)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_coat}'

class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_jacket = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_jacket}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_square_full)
print(jacket.get_square_full)
print(jacket.get_square_coat())
print(jacket.get_square_jacket())
