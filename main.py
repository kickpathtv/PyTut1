import KP, pygame

class Window:
    def draw(self, screen, dt, t):
        point = (20, 20)
        radius = 5
        c1 = pygame.draw.circle(
            screen,
            KP.RED,
            (int(10 * dt), 20),
            radius
            )

if __name__ == "__main__":
    e = KP.WithWindow(Window())