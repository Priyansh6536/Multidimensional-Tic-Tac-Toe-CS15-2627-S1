restart_match = True

def display_grid(grid):
    for row in grid:
        print(row)

def determine_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
        else:
            pass

    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] and grid[0][column] != "":
            return grid[0][column]
        else:
            pass

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        return grid[0][2]
    else:
        pass

    return "Tie"


while True:
    if restart_match == True:
        match_grid = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        restart_match = False



    while True:
        display_grid(match_grid)
        while True:
            player_1_row = input("Player 1, choose the row:\n")
            try:
                player_1_row = int(player_1_row.strip())
                if player_1_row in range(1, 4):
                    break
                else:
                    print("You need to enter a number between 1-3")
            except ValueError:
                print("You need to enter a number between 1-3")

        while True:
            player_1_column = input("Player 1, choose the column:\n")
            try:
                player_1_column = int(player_1_column.strip())
                if player_1_column in range(1, 4):
                    break
                else:
                    print("You need to enter a number between 1-3")
            except ValueError:
                print("You need to enter a number between 1-3")

        if match_grid[player_1_row - 1][player_1_column - 1] == "":
            match_grid[player_1_row - 1][player_1_column - 1] = "X"
            break
        else:
            print("That space is already occupied")

    if determine_winner(match_grid) == "X":
        print("The winner is X")
        restart_match = True
        continue
    elif determine_winner(match_grid) == "Tie":
        full_rows = 0

        for row in match_grid:
            if row[0] != "" and row[1] != "" and row[2] != "":
                full_rows += 1

        if full_rows == 3:
            print("The match is a Tie")
            restart_match = True
            continue
    else:
        pass
    while True:
        display_grid(match_grid)

        while True:
            player_2_row = input("Player 2, choose the row:\n")
            try:
                player_2_row = int(player_2_row.strip())
                if player_2_row in range(1, 4):
                    break
                else:
                    print("You need to enter a number between 1-3")
            except ValueError:
                print("You need to enter a number between 1-3")

        while True:
            player_2_column = input("Player 2, choose the column:\n")
            try:
                player_2_column = int(player_2_column.strip())
                if player_2_column in range(1, 4):
                    break
                else:
                    print("You need to enter a number between 1-3")
            except ValueError:
                print("You need to enter a number between 1-3")

        if match_grid[player_2_row - 1][player_2_column - 1] == "":
            match_grid[player_2_row - 1][player_2_column - 1] = "O"
            break
        else:
            print("That space is already occupied")


    if determine_winner(match_grid) == "O":
        print("The winner is O")
        restart_match = True
    elif determine_winner(match_grid) == "Tie":
        full_rows = 0

        for row in match_grid:
            if row[0] != "" and row[1] != "" and row[2] != "":
                full_rows += 1

        if full_rows == 3:
            print("The match is a Tie")
            restart_match = True
    else:
        pass