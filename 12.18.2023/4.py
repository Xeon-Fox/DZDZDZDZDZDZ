list=[2, 5, 8, 9, 4]
min_index = list.index(min(list))
max_index = list.index(max(list))

distance=min_index-max_index
print(abs(distance)) # как я понял абс просто минус убирает