numbers1 = {1, 3, 5, 7, 9}
numbers2 = {2, 4, 6, 8, 10}
numbers3 = {7, 9, 5, 2, 1, 3}

numbers_union= numbers1.union(numbers2)
print(numbers_union)

numbers_intersection= numbers2.intersection(numbers3)
print(numbers_intersection)

numbers_different= numbers2.difference(numbers3)
print(numbers_different)

numbers_symmdiff= numbers3.symmetric_difference(numbers1)
print(numbers_symmdiff)