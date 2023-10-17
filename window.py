# Example file showing a basic pygame "game loop"
import pygame
from pygame import draw, Surface
from implementation_one import *

qt_line = 30
size = 20
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1270, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
left_button_clicked = False

grid = create_grid(10)

def draw_grid(screen: Surface):
    center_x = screen.get_width() / 2
    center_y = screen.get_height() / 2
    start_x = (center_x - (len(grid) * size) / 2)
    start_y = (center_y - (len(grid) * size) / 2)
    for x in range(len(grid)):
        pos_x = x * size + start_x
        for y in range(len(grid)):
            pos_y = y * size + start_y
            if grid[x][y] == 0:
                draw.rect(screen, "white", (pos_x, pos_y, size, size), 1)
            if grid[x][y] == 1:
                draw.rect(screen, "white", (pos_x, pos_y, size, size), 10)


# def draw_grid():
#    for x in range(qt):
#        for y in range(qt):
#            draw.rect(screen, "white", (x * size, y * size, size, size), 1)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    draw_grid(screen)

    # Get the state of mouse buttons
    mouse_buttons = pygame.mouse.get_pressed()

    # Check for left, middle, and right mouse button clicks
    if mouse_buttons[0] and not left_button_clicked:
        grid = create_grid(10)
        left_button_clicked = True

        # Reset the flag when the button is released
    if not mouse_buttons[0]:
        left_button_clicked = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
