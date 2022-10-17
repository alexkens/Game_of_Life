
# cell constants
#NOTHING = 0
ALIVE = 1
DEAD = 0

BASE = 10


def create_grid():
    return [0 for i in range(BASE*BASE)]


def print_grid(grid, base):
    print("My Grid")

    print("------------")
    for i in range(base):
        print("|", end='')
        for j in range(base):
            if grid[i*base + j] == ALIVE:
                print("o", end='')
            elif grid[i*base + j] == ALIVE:
                print(" ", end='')
            else:
                print(" ", end='')
        print("|", end='')
        print()
    print("------------")
    print()


def insert_life(grid, l):
    for e in l:
        grid[e] = 1
    return grid


# R1 alive cell < 2 neighbours --> dead
# R2 alive cell > 3 neighbours --> dead
# R3 alive cell == 2,3 neighbours --> alive
# R4 dead cell == 3 neighbours --> alive
def play(grid):

    updated_grid = grid.copy()

    for cell_index in range(len(grid)):
        cell_neighbours = neighbours(cell_index, grid)

        """if cell_index == 45:
            print(cell_index)
            print(grid[cell_index])
            print(cell_neighbours)"""

        if grid[cell_index] == ALIVE:
            if cell_neighbours < 2 or cell_neighbours > 3:
                updated_grid[cell_index] = DEAD
        elif grid[cell_index] == DEAD:
            if cell_neighbours == 3:
                updated_grid[cell_index] = ALIVE
        else:
            continue

    return updated_grid


def neighbours(cell, grid):
    cell_neighbours = 0
    up_row = [cell-BASE-1, cell-BASE, cell-BASE+1]
    in_row = [cell-1, cell+1]
    low_row = [cell+BASE-1, cell+BASE, cell+BASE+1]
    l = up_row + in_row + low_row

    for e in l:
        if 0 < e < 100:
            if grid[e] == ALIVE:
                cell_neighbours += 1

    # print(cell)
    # print(cell_neighbours)

    return cell_neighbours


if __name__ == '__main__':
    grid = create_grid()
    print_grid(grid, BASE)

    l = [44, 45, 46]
    l1 = [44, 45, 46, 54, 56, 64, 65, 66]
    insert_life(grid, l1)
    print_grid(grid, BASE)

    for i in range(15):
        grid = play(grid)
        print_grid(grid, BASE)
