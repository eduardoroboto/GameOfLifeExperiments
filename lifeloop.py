import pygame
from pygame import draw, Surface
from pygame.locals import *
from typing import Callable


class GameOfLifeWindow:
    def __init__(self):
        self.grid = None
        self.qt_line = 30
        self.size = 20
        self.game = pygame.init()
        self.screen = pygame.display.set_mode((1270, 720), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.left_button_clicked = False
        self.grid_size = 25
        self.start = False

        self.run_generation = None
        self.create_grid = None
        self.randomize_matrix = None
        self.draw_data = None
        self.add_column = None
        self.remove_column = None
        self.add_row = None
        self.remove_row = None

    def add_create_grid_logic(self, logic: Callable):
        self.create_grid = logic
        return self

    def add_draw_logic(self, logic: Callable):
        self.draw_data = logic
        return self

    def add_add_column_logic(self, logic: Callable):
        self.add_column = logic
        return self

    def add_add_row_logic(self, logic: Callable):
        self.add_row = logic
        return self

    def add_remove_column_logic(self, logic: Callable):
        self.remove_column = logic
        return self

    def add_remove_row_logic(self, logic: Callable):
        self.remove_row = logic
        return self

    def add_run_generation_logic(self, logic: Callable):
        self.run_generation = logic
        return self

    def add_randomize_matrix(self,logic:Callable):
        self.randomize_matrix = logic
        return self

    def init_grid(self) -> None:
        self.grid = self.create_grid(self.grid_size)

    @staticmethod
    def draw_cell_standard(screen: Surface, cell_value: int, pos_x: float, pos_y: float, size: int) -> None:
        if cell_value == 0:
            draw.rect(screen, "white", (pos_x, pos_y, size, size))
        elif cell_value == 1:
            draw.rect(screen, "white", (pos_x, pos_y, size, size), 1)

    def draw_grid(self, screen: Surface) -> None:
        self.draw_data(screen, self.grid, self.size, self.draw_cell_standard)

    def switch_start(self) -> None:
        self.start = not self.start

    def run(self) -> None:
        while self.running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == MOUSEWHEEL:
                    if event.y > 0:
                        self.size += 1
                    elif event.y < 0:
                        self.size -= 1

            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.switch_start()
            if keys[K_UP]:
                self.add_column(self.grid)
            elif keys[K_DOWN]:
                self.remove_column(self.grid)
            if keys[K_LEFT]:
                self.add_row(self.grid)
            elif keys[K_RIGHT]:
                self.remove_row(self.grid)
            elif keys[K_ESCAPE]:
                self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")
            self.draw_grid(self.screen)

            # Get the state of mouse buttons
            mouse_buttons = pygame.mouse.get_pressed()

            # Check for left, middle, and right mouse button clicks
            if mouse_buttons[0] and not self.left_button_clicked:
                self.randomize_matrix(self.grid)
                left_button_clicked = True

                # Reset the flag when the button is released
            if not mouse_buttons[0]:
                left_button_clicked = False

            # RENDER YOUR GAME HERE
            # flip() the display to put your work on screen
            pygame.display.flip()
            if self.start:
                self.grid = self.run_generation(self.grid)
            self.clock.tick(15)  # limits FPS to 60

        pygame.quit()
