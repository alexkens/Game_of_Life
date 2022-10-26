


# Constants: ALIVE, DEAD, grid_size, base
ALIVE = 1
DEAD = 0
BASE = 10
GRID_SIZE = BASE*BASE

def create_grid():
    grid = []
    for i in range(GRID_SIZE):
        grid.append(DEAD)
    return grid

def print_grid(grid, base):
    print("My Grid")

    print("------------")
    for i in range(base):
        print("|", end='')
        for j in range(base):
            if grid[i * base + j] == ALIVE:
                print("o", end='')
            elif grid[i * base + j] == ALIVE:
                print(" ", end='')
            else:
                print(" ", end='')
        print("|", end='')
        print()
    print("------------")
    print()

def insert_life(grid, insert_list):
    for index in insert_list:
        grid[index] = ALIVE
    return grid


# R3 alive cell == 2,3 neighbours --> alive
# R4 dead cell == 3 neighbours --> alive

def step(grid):
    upgrade_grid = grid.copy()

    for cell_index in range(GRID_SIZE):
        n = neighbours(cell_index, grid)
        if grid[cell_index] == ALIVE:
            if n == 2 or n == 3:
                continue
            else:
                upgrade_grid[cell_index] = DEAD
        if grid[cell_index] == DEAD:
            if n == 3:
                upgrade_grid[cell_index] = ALIVE

    return upgrade_grid


def neighbours(cell_index, grid):
    n_count = 0

    up_row = [cell_index-BASE-1, cell_index-BASE, cell_index-BASE+1]
    in_row = [cell_index-1, cell_index+1]
    low_row = [cell_index+BASE-1, cell_index+BASE, cell_index+BASE+1]
    l = up_row + in_row + low_row

    for element in l:
        if 0 <= element < 100:
            if grid[element] == ALIVE:
                n_count += 1

    return n_count



if __name__ == '__main__':

    # create grid
    grid = create_grid()

    # print grid
    print_grid(grid, BASE)

    # insert life
    insert_list = [55, 56, 57, 65, 67, 75, 76, 77]
    grid = insert_life(grid, insert_list)
    print_grid(grid, BASE)

    # step, neighbours
    grid = step(grid)
    print_grid(grid, BASE)

    grid = step(grid)
    print_grid(grid, BASE)

    grid = step(grid)
    print_grid(grid, BASE)

