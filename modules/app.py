import pygame


class App(object):
    def __init__(self, size: list, fps: int, caption: str):
        self.fps = fps
        self.size = size
        self.running = True
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption(caption)
        pygame.init()

    def draw(self):
        self.screen.fill([20, 20, 20])
        pygame.display.flip()

    def update(self):
        pass

    def run(self):
        while self.running:
            self.update()
            self.draw()
            self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
