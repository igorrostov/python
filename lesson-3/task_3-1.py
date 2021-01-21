def div(*args):

    try:
        arg1 = int(input("Делимое "))
        arg2 = int(input("Делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''


print(f'Частное  {div()}')
