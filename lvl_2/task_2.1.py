# Задача 2.1.

def minimum(arr):
    minimum_number = arr[0]
    for element_1 in arr:
        if element_1 < minimum_number:
            minimum_number = element_1
    return minimum_number


def maximum(arr):
    maximum_number = arr[0]
    for element_2 in arr:
        if element_2 > maximum_number:
            maximum_number = element_2
    return maximum_number


list_numbers = [-52, 56, 30, 29, -54, 0, -110]
result_2 = maximum(list_numbers)
result_1 = minimum(list_numbers)
print('min =', result_1, 'max =', result_2)
