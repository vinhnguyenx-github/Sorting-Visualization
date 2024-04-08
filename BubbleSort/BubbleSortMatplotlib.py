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
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                update_plot(data, bars)
                plt.pause(0.1)

bubble_sort_visualization(values, ax)
plt.pause(1) 
plt.show()
