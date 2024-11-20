from lifeloop import GameOfLifeWindow
from implementation_one import *


def main():
    game = (GameOfLifeWindow()
            .add_run_generation_logic(run_generation)
            .add_randomize_matrix(randomize_matrix)
            .add_create_grid_logic(create_grid)
            .add_draw_logic(draw_grid_logic_list)
            .add_add_column_logic(add_column)
            .add_add_row_logic(add_row)
            .add_remove_column_logic(remove_column)
            .add_remove_row_logic(remove_row))

    game.init_grid()
    game.run()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
