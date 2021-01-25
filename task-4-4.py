my_list = [1, 3, 3, 3, 7, 7, 8, 8, 5, 4]
my_List_new = [el for el in my_list if my_list.count(el) < 2]
print(my_List_new)
