import KP, pygame


if __name__ == "__main__":
    KP.WithDrawFunction(lambda screen, delta_time :
        pygame.draw.circle(
                screen,
                (255, 0, 0),
                (20, 20),
                10
            )
    )