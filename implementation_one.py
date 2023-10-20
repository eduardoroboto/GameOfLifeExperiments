import random


def randomize_matrix(matrix):
    for row in matrix:
        for i in range(len(row)):
            row[i] = random.choice([0, 1])
    return matrix

def create_grid(size: int) -> list:
    f = int(size / 2)
    weights = [0.6, 0.3]  # Adjust the weights to control the distribution (more 0s than 1s)

    return [[random.choices([0, 1], weights=weights)[0] for _ in range(size)] for _ in range(size)]

def create_matrix(x:int, y:int, value=0) -> list:
    return [[value for _ in range(y)] for _ in range(x)]


def resize_matrix(matrix, new_x, new_y):
    if new_x > len(matrix):
        for _ in range(new_x - len(matrix)):
            matrix.append([random.choice([0, 1]) for _ in range(len(matrix[0]))])
    else:
        matrix = matrix[:new_x]

    for row in matrix:
        if new_y > len(row):
            row.extend([random.choice([0, 1]) for _ in range(new_y - len(row))])
        else:
            row = row[:new_y]

    return matrix

def add_row(matrix):
    if len(matrix) == 0:
        return [[random.choice([0, 1])]]
    new_row_one = [random.choice([0, 1]) for _ in range(len(matrix[0]))]
    new_row_two = [random.choice([0, 1]) for _ in range(len(matrix[0]))]
    matrix.append(new_row_one)
    matrix.insert(0,new_row_two)
    return matrix

def add_column(matrix):
    if len(matrix) == 0:
        return [[random.choice([0, 1])]]
    for row in matrix:
        row.append(random.choice([0, 1]))
        row.insert(0,random.choice([0, 1]))
    return matrix

def remove_row(matrix):
    if len(matrix) == 0:
        return matrix
    matrix.pop()
    matrix.pop(0)
    return matrix

def remove_column(matrix):
    if len(matrix) == 0:
        return matrix
    for row in matrix:
        if len(row) > 0:
            row.pop()
            row.pop(0)
    return matrix

def bigger_matrix(matrix):
    add_row(matrix)
    add_column(matrix)

def smalled_matrix(matrix):
    remove_column(matrix)
    remove_row(matrix)

# def create_grid(size: int) -> list:
#     grid = [[0 for _ in range(size)] for _ in range(size)]  # Initialize the grid with all 0s
#
#     # Define the Glider pattern
#     glider = [[0, 1, 0],
#               [0, 0, 1],
#               [1, 1, 1]]
#
#     # Place the Glider at a specific location (e.g., top-left corner)
#     for i in range(len(glider)):
#         for j in range(len(glider[0])):
#             grid[i+1][j+1] = glider[i][j]
#
#     return grid


# def create_clean_grid(size: int) -> list:
#     f = int(size/2)
#     return [[0] * size for _ in range(size)]
#

def add_rows(size:int, grid:list):
    grid.append([0]*size)
def add_cols(size:int, grid:list):
    for i in range(size):
        grid[i].append(0)



def get_neighbors(grid:list,x:int,y:int):
    rows =  len(grid)
    cols = len(grid[0])
    if( 0 <= x < rows and 0 <= y < cols):
        #one
        yield grid[x-1][y-1] if x > 0 and y>0 else None
        #two
        yield grid[x-1][y] if x > 0 else None
        #three
        yield grid[x-1][y+1] if x > 0 and y < cols - 1  else None
        #four
        yield grid[x][y-1] if y > 0 else None
        #original
        #yield grid[x][y]
        #five
        yield grid[x][y+1] if y < cols - 1 else None
        #six
        yield grid[x+1][y-1] if x < rows - 1 and y > 0 else None
        #seven
        yield grid[x+1][y] if x < rows - 1 else None
        #eigth
        yield grid[x+1][y+1] if x < rows - 1 and  y < cols - 1  else None


def live_or_die(grid:list,x:int,y:int) -> bool:
    live_neighbors = sum(item for item in get_neighbors(grid, x, y) if item is not None)
    cell_state = grid[x][y]

    if cell_state == 1:
        if live_neighbors == 2 or live_neighbors == 3:
            return True
        else:
            return False
    else:
        if live_neighbors == 3:
            return True
        else:
            return False


def run_generation(grid:list):
    rows = len(grid)
    cols = len(grid[0])
    next_gen = create_matrix(rows, cols,0)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if live_or_die(grid,x,y):
                next_gen[x][y] = 1
            else:
                next_gen[x][y] = 0
    return next_gen


#if __name__ == '__main__':
#    test = create_grid(10)
#    ok = list(get_neighbors(test,4,4))


