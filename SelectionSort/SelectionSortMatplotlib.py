import matplotlib.pyplot as plt
import numpy as np

n = 100

values = np.random.randint(1, 40, n)
index = np.arange(0, n, 1)

fig, ax = plt.subplots(figsize = (12, 6))
bars = ax.bar(index, values)
ax.set_title('Selection Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_xticks(np.arange(0, n, 1))

def update_plot(heights, bars):
    for bar, height in zip(bars, heights):
        bar.set_height(height)

def bubble_sort_visualization(data, ax):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
                plt.pause(0.00001)

        data[i], data[min_index] = data[min_index], data[i]
        update_plot(data, bars)
        plt.pause(0.00001)

bubble_sort_visualization(values, ax)
plt.show()
