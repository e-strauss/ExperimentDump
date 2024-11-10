import numpy as np
import math


np.random.seed(7)

list_sorted = []
for i in range(9):
    list_sorted.append(i)

print(list_sorted)

list_unsorted = list(np.random.permutation(list_sorted))

print(list_unsorted)


def minimum(list_input):
    if len(list_input) == 0:
        return None
    current_min = list_input[0]
    for j in range(1, len(list_input)):
        if list_input[j] < current_min:
            current_min = list_input[j]
    return current_min


def index_minimum(list_input):
    if len(list_input) == 0:
        return None
    current_min = list_input[0]
    current_index = 0
    for j in range(1, len(list_input)):
        if list_input[j] < current_min:
            current_min = list_input[j]
            current_index = j
    return current_index


print(minimum(list_unsorted))
print(index_minimum(list_unsorted))


def sort1(list_input):
    new_sorted_list = []
    while len(list_input) > 0:
        new_minimum_index = index_minimum(list_input)
        new_sorted_list.append(list_input[new_minimum_index])
        list_input.pop(new_minimum_index)
    return new_sorted_list


new_list = sort1(list_unsorted.copy())
print(new_list)


def sort2(list_input):
    for k in range(len(list_input)):
        j = k
        current = list_input[j]
        while j - 1 >= 0 and current < list_input[j - 1]:
            list_input[j] = list_input[j - 1]
            j = j - 1
        list_input[j] = current
    return list_input


new_list = sort2(list_unsorted.copy())
print(new_list)


def sort3(list_input):
    size = len(list_input)
    window_size = 1
    while window_size < size:
        for a in range(math.ceil(size / (2 * window_size))):
            a = a * 2 * window_size
            b = a + window_size
            b_end = min(size, a + 2*window_size)
            while b < b_end and list_input[b - 1] > list_input[b]:
                current = list_input[b]
                list_input[b] = list_input[b - 1]
                a_tmp = b - 2
                while list_input[a_tmp] > current and a_tmp >= a:
                    list_input[a_tmp + 1] = list_input[a_tmp]
                    a_tmp = a_tmp - 1
                list_input[a_tmp + 1] = current
                b = b + 1
    return list_input


print(list_unsorted)
new_list = sort3(list_unsorted.copy())
print(new_list)
