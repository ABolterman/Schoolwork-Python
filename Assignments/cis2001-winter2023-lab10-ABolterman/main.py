# time counting adapted from :
# https://github.com/EricCharnesky/CIS2001-Winter2023/blob/main/Week4-ArrayBasedSequences/main.py#L19-L33
import time
import random


def compute_time_to_sort_built_in(list_to_sort):
    start = time.perf_counter()
    list_to_sort.sort()
    end = time.perf_counter()
    return end-start


def compute_time_to_sort_selection(list_to_sort):
    start = time.perf_counter()
    selection_sort(list_to_sort)
    end = time.perf_counter()
    return end-start


def compute_time_to_sort_insertion(list_to_sort):
    start = time.perf_counter()
    insertion_sort(list_to_sort)
    end = time.perf_counter()
    return end-start


def selection_sort(list_to_sort):
    for current_index in range(len(list_to_sort) - 1):
        smallest_value_index = current_index
        for index_to_check in range(current_index+1, len(list_to_sort)):
            if list_to_sort[index_to_check] < list_to_sort[smallest_value_index]:
                smallest_value_index = index_to_check
        temp = list_to_sort[current_index]
        list_to_sort[current_index] = list_to_sort[smallest_value_index]
        list_to_sort[smallest_value_index] = temp


def insertion_sort(list_to_sort):
    for current_index in range(1, len(list_to_sort)):
        while current_index > 0 and list_to_sort[current_index] < list_to_sort[current_index - 1]:
            temp = list_to_sort[current_index]
            list_to_sort[current_index] = list_to_sort[current_index - 1]
            list_to_sort[current_index - 1] = temp
            current_index -= 1


some_list = []
for n in range(10):
    some_list.append(random.randint(0, 50000))
bi_list = ss_list = is_list = some_list

print(f"Built-in: {compute_time_to_sort_built_in(bi_list)}")
print(f"Selection Sort: {compute_time_to_sort_selection(ss_list)}")
print(f"Insertion Sort: {compute_time_to_sort_insertion(is_list)}")

# Fastest to slowest - Insertion, Built-in, Selection

