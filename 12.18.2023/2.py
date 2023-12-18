list = [5, 2, 3, 1, 10]
max_in_list = max(list)
minspisol = min(list)
index_of_max_num = list.index(max_in_list)
index_of_min_num = list.index(minspisol)

list.pop(index_of_max_num)
list.pop(index_of_min_num)

list.insert(index_of_min_num, max_in_list)
list.insert(index_of_max_num, minspisol)

print(list)
