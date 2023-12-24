list1 = [1, 2, 4, 3, 5, 7]
list2 = [2, 3, 4]
for i in list2:
    if i in list1:
        list1.remove(i)
print(list1)