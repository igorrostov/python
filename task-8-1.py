class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Всё хорошо'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая data {Data.extract(self.day_month_year)}'


today = Data('08 - 02 - 2021')
print(today)
print(Data.valid(20, 12, 2022))
print(today.valid(20, 15, 2012))
print(Data.extract('20 - 12 - 2022'))
print(today.extract('20 - 15 - 2020'))
print(Data.valid(1, 11, 2001))
