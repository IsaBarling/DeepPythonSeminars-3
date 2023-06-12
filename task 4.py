# Создание списка с повторяющимися элементами
my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 5, 9, 1, 10, 11, 6]

# Создание словаря для подсчета количества повторений каждого элемента
count_dict = {}
for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1

# Удаление элементов, которые встречаются дважды
new_list = [item for item in my_list if count_dict[item] != 2]

# Вывод результата
print(new_list)
