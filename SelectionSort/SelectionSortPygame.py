import pygame
import numpy

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
        self.dataWidth = 1
        self.totalDataPoints = self.screen_width // self.dataWidth
        self.dataLength = numpy.random.randint(10, self.screen_height - 50, self.totalDataPoints)
        self.states = numpy.zeros((self.totalDataPoints,), dtype=int)
        self.counter = 0

    def draw(self):
        for i in range(len(self.dataLength)):
            color = WHITE if self.states[i] == 0 else (RED if self.states[i] == 1 else GREEN)
            pygame.draw.rect(self.screen, color,
                             (i * self.dataWidth, self.screen_height - self.dataLength[i],
                              self.dataWidth, self.dataLength[i]))

    def selection_sort(self):
        if self.counter < self.totalDataPoints:
            min_index = self.counter
            for j in range(self.counter + 1, self.totalDataPoints):
                if self.dataLength[j] < self.dataLength[min_index]:
                    min_index = j

            self.states[min_index] = 1
            self.dataLength[self.counter], self.dataLength[min_index] = self.dataLength[min_index], self.dataLength[self.counter]
            self.states[self.counter] = 2

        self.counter += 1

def main():
    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    graph = Graph(screen, screen_width, screen_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        graph.draw()
        graph.selection_sort()

        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
