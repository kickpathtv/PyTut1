import pygame, math

BLUE = (90, 90, 255)
RED = (255, 90, 90)

class WithWindow:
    def __init__(self, window):
        self.clock = pygame.time.Clock()
        self.w = window
        # Time elapsed since start
        self.t = 0
        self.loop()
    def loop(self):
        screen = pygame.display.set_mode((400, 400))
        running = True
        i = 0
        screen = pygame.display.get_surface()
        while running:
            screen.fill(pygame.Color(60, 60, 85))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            i += 1
            _i_time = self.clock.get_time()
            self.t = self.t + _i_time
            self.w.draw(screen, _i_time, self.t)
            pygame.display.flip()
            self.clock.tick()
        pygame.quit()