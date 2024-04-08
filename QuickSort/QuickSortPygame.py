import pygame
import numpy as np
import sys  # Import the sys module

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (34, 255, 0)

class Graph:
    def __init__(self, screen, screen_width, screen_height) -> None:
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.dataWidth = 30
        self.totalDataPoints = self.screen_width // self.dataWidth
        self.dataLength = np.random.randint(10, self.screen_height - 50, self.totalDataPoints)
        self.states = np.zeros((self.totalDataPoints,), dtype=int)
        self.counter = 0

    def draw(self):
        self.screen.fill(BLACK)
        for i in range(len(self.dataLength)):
            color = WHITE if self.states[i] == 0 else (RED if self.states[i] == 1 else GREEN)
            pygame.draw.rect(self.screen, color,
                             (i * self.dataWidth, self.screen_height - self.dataLength[i],
                              self.dataWidth, self.dataLength[i]))
        pygame.display.update()

    def find_pivot(self, low, high):
        pivot = self.dataLength[high]
        index = low
        for i in range (low, high):
            if self.dataLength[i] < pivot:
                self.states[i] = 1
                self.states[index] = 1
                self.dataLength[index], self.dataLength[i] = self.dataLength[i], self.dataLength[index]
                index += 1
        self.dataLength[high] = self.dataLength[index]
        self.dataLength[index] = pivot
        self.states[index] = 2
        return index

    def quick_sort(self, low, high):
        if low < high:
            index = self.find_pivot(low, high)
            self.draw()  # Update visualization after each step
            pygame.time.wait(10)  # Pause for visualization
            self.quick_sort(low, index - 1)
            self.quick_sort(index+1, high)

def main():
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    graph = Graph(screen, screen_width, screen_height)

    sys.setrecursionlimit(10**6)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        graph.quick_sort(0, graph.totalDataPoints-1)  # Moved sorting inside the main loop
        clock.tick(60)  # Adjust the speed as needed
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
