import matplotlib.pyplot as plt
import numpy as np

n = 100

values = np.random.randint(1, 40, n)
index = np.arange(0, n, 1)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(index, values)
ax.set_title('Quick Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_xticks(np.arange(0, n, 1))

def update_plot(heights, bars):
    for bar, height in zip(bars, heights):
        bar.set_height(height)

def find_pivot(data, low, high):
    pivot = data[high]
    index = low
    for i in range (low, high):
        if data[i] <= pivot:
            data[index], data[i] = data[i], data[index]
            update_plot(data, bars)
            plt.pause(0.00001)
            index += 1
    data[high], data[index] = data[index], data[high]
    update_plot(data, bars)
    plt.pause(0.0001)
    return index

def quick_sort_visualization(data, ax, low, high):
    if low < high:
        pivot_index = find_pivot(data, low, high)
        quick_sort_visualization(data, ax, low, pivot_index - 1)
        quick_sort_visualization(data, ax, pivot_index + 1, high)

quick_sort_visualization(values, ax, 0, len(values) - 1)
plt.show()
