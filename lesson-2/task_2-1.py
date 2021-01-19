my_list = [3, 1.3, -3, None, False, 'List']
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
