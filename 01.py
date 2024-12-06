# https://github.com/lapsheva/PyGame2024.git

import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Мишень')
    try:
        w, n = map(int, input().split())
    except Exception:
        print('Неправильный формат ввода')
        return None

    size = (2 * n * w, 2 * n * w)
    screen = pygame.display.set_mode(size)
    draw(screen, w, n)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def draw(screen, w, n):
    colors = (pygame.Color('red'), pygame.Color('green'),
              pygame.Color('blue'))
    rad = w * n
    centre = (rad, rad)
    for i in range(n, -1, -1):
        pygame.draw.circle(screen, colors[(i + 2) % 3],
                           centre, rad, 0)
        rad = rad - w


if __name__ == "__main__":
    sys.exit(main())