my_list = [86, 76, 12, 22, 46, 67, 97]
my_list_new = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {my_list_new}')
