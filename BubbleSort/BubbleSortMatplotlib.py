import matplotlib.pyplot as plt
import numpy as np

n = 100

values = np.random.randint(1, 40, n)
index = np.arange(0, n, 1)

fig, ax = plt.subplots(figsize = (12, 6))
bars = ax.bar(index, values)
ax.set_title('Bubble Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_xticks(np.arange(0, n, 1))

def update_plot(heights, bars):
    for bar, height in zip(bars, heights):
        bar.set_height(height)

def bubble_sort_visualization(data, ax):
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                update_plot(data, bars)
                plt.pause(0.00001)
        if not swapped:
            break

bubble_sort_visualization(values, ax)
plt.show()
