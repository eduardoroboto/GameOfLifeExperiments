# Example file showing a basic pygame "game loop"
import pygame
from pygame import draw, Surface
from implementation_one import *
from pygame.locals import *

qt_line = 30
size = 20
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1270, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
left_button_clicked = False

grid_size = 25
grid = create_grid(grid_size)
start = False


def draw_grid(screen: Surface):
    center_x = screen.get_width() / 2
    center_y = screen.get_height() / 2
    start_x = (center_x - (len(grid) * size) / 2)
    start_y = (center_y - (len(grid[0]) * size) / 2)
    for x in range(len(grid)):
        pos_x = x * size + start_x
        for y in range(len(grid[x])):
            pos_y = y * size + start_y
            if grid[x][y] == 0:
                draw.rect(screen, "white", (pos_x, pos_y, size, size))
            if grid[x][y] == 1:
                draw.rect(screen, "white", (pos_x, pos_y, size, size), 1)


while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == MOUSEWHEEL:
            if event.y > 0:
                size += 1
            elif event.y < 0:
                size -= 1

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        start = not start
    if keys[K_UP]:
        add_column(grid)
    elif keys[K_DOWN]:
        remove_column(grid)
    if keys[K_LEFT]:
        add_row(grid)
    elif keys[K_RIGHT]:
        remove_row(grid)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    draw_grid(screen)

    # Get the state of mouse buttons
    mouse_buttons = pygame.mouse.get_pressed()

    # Check for left, middle, and right mouse button clicks
    if mouse_buttons[0] and not left_button_clicked:
        randomize_matrix(grid)
        left_button_clicked = True

        # Reset the flag when the button is released
    if not mouse_buttons[0]:
        left_button_clicked = False

    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()
    if start:
        grid = run_generation(grid)
    clock.tick(15)  # limits FPS to 60

pygame.quit()
