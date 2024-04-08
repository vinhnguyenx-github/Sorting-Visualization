import pygame
import random

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
        self.dataLength = [random.randint(10, self.screen_height - 50) for _ in range(self.totalDataPoints)]
        self.states = [0 for _ in range(self.totalDataPoints)]
        self.counter = 0

    def draw(self):
        for i in range(len(self.dataLength)):
            color = WHITE if self.states[i] == 0 else (RED if self.states[i] == 1 else GREEN)
            pygame.draw.rect(self.screen, color,
                             (i * self.dataWidth, self.screen_height - self.dataLength[i],
                              self.dataWidth, self.dataLength[i]))

    def bubble_sort(self):
        if self.counter < self.totalDataPoints:
            for j in range(self.totalDataPoints - 1 - self.counter):
                if self.dataLength[j] > self.dataLength[j+1]:
                    self.states[j] = 0
                    self.states[j+1] = 0
                    self.dataLength[j], self.dataLength[j+1] =  self.dataLength[j+1], self.dataLength[j]
                else:
                    self.states[j] = 1
                    self.states[j+1] = 1
                    
        self.counter += 1
        
        if self.totalDataPoints - self.counter >= 0:
            self.states[self.totalDataPoints - self.counter] = 2

def main():
    screen_width = 600
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
        graph.bubble_sort()

        clock.tick(90)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
