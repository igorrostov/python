def sal():
    try:
        time = float(input('Выработка в часах (в месяц): '))
        salary = int(input('Ставка в рублях (в час) : '))
        bonus = int(input('Премия в рублях (в месяц): '))
        result = time * salary + bonus
        print(f'Заработная плата сотрудника: {result} ')
    except ValueError:
        return print('Введите число: ')
sal()
