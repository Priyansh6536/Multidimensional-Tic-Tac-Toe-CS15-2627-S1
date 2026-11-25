grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]


def display_grid(grid):
    for row in grid:
        print(row)

def determine_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2]:
            return row[0]
        else:
            pass
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column]:
            return grid[0][column]
        else:
            pass
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]
    else:
        pass
    return "Tie"

for grid in [grid_1, grid_2, grid_3, grid_4]:
    display_grid(grid)
    print(f"Winner: {determine_winner(grid)}\n")


