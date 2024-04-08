import matplotlib.pyplot as plt
import numpy as np

n = 20

values = np.random.randint(1, 50, n)
index = np.arange(0, n, 1)

fig, ax = plt.subplots()
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
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
        update_plot(data, bars)
        plt.pause(1)

bubble_sort_visualization(values, ax)
plt.pause(1) 
plt.show()
