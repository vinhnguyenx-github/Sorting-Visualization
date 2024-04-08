import matplotlib.pyplot as plt
import numpy as np
import time

# Define the sorting algorithms
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break

def insert_sort(data):
    for i in range (1, len(data)):
        key = data[i]
        j = i -1

        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j=j-1
            
        data[j+1] = key

def quick_sort(data, low, high):
    if low < high:
        pivot_index = partition(data, low, high)
        quick_sort(data, low, pivot_index - 1)
        quick_sort(data, pivot_index + 1, high)

def partition(data, low, high):
    pivot = data[high]
    index = low
    for i in range(low, high):
        if data[i] <= pivot:
            data[index], data[i] = data[i], data[index]
            index += 1
    data[high], data[index] = data[index], data[high]
    return index

# Generate random data
n = 10000
values_selection = np.random.randint(1, 40, n).tolist()
values_bubble = values_selection.copy()
values_quick = values_selection.copy()
values_insert = values_selection.copy()

# Measure and compare execution time
start_time = time.time()
selection_sort(values_selection)
selection_time = time.time() - start_time

start_time = time.time()
bubble_sort(values_bubble)
bubble_time = time.time() - start_time

start_time = time.time()
quick_sort(values_quick, 0, len(values_quick) - 1)
quick_time = time.time() - start_time

start_time = time.time()
insert_sort(values_insert)
insertion_time = time.time() - start_time

print("Selection Sort Time:", selection_time)
print("Bubble Sort Time:", bubble_time)
print("Quick Sort Time:", quick_time)
print("Insertion Sort Time:", insertion_time)
