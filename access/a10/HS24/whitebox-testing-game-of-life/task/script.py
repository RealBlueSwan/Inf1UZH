#!/usr/bin/env python3

def evolve(world, steps):
    # Validate input parameters
    if not isinstance(world, tuple) or not all(isinstance(row, str) for row in world):
        raise Warning("Invalid world: must be a tuple of strings")
    if not all(len(row) == len(world[0]) for row in world):
        raise Warning("Invalid world: all rows must have the same length")
    if len(world) <= 2 or len(world[0]) <= 2:
        raise Warning("Invalid world: dimensions must be greater than 2")
    if not all(char in "-|# " for row in world for char in row):
        raise Warning("Invalid character in world")
    if not isinstance(steps, int) or steps <= 0:
        raise Warning("Invalid steps: must be a positive integer")

    current_world = [list(row) for row in world]  # Convert tuple of strings to list of lists for mutability
    for _ in range(steps):  # This has to run for n steps
        new_world = []
        for row_idx in range(len(current_world)):
            new_row = []
            for char_idx in range(len(current_world[row_idx])):
                # This starts at 0, 0
                if current_world[row_idx][char_idx] in ('-', '|'):
                    new_row.append(current_world[row_idx][char_idx])
                elif current_world[row_idx][char_idx] in (' ', '#'):
                    alive_in_proximity = alive_counter(current_world, row_idx, char_idx, False)
                    if current_world[row_idx][char_idx] == '#' and alive_in_proximity < 2:
                        new_row.append(' ')
                    elif current_world[row_idx][char_idx] == '#' and alive_in_proximity > 3:
                        new_row.append(' ')
                    elif current_world[row_idx][char_idx] == '#' and alive_in_proximity in (2, 3):
                        new_row.append('#')
                    elif current_world[row_idx][char_idx] == ' ' and alive_in_proximity == 3:
                        new_row.append('#')
                    else:
                        new_row.append(current_world[row_idx][char_idx])
            new_world.append(new_row)
        current_world = new_world

    return_board = tuple(''.join(row) for row in current_world)
    return (return_board, alive_counter(current_world, 0, 0, True))

def alive_counter(board, current_row, current_char, full=True, radius=1):
    # Keep in mind to check if the index is an edge point!
    if full:  # This will count the whole board
        counter = sum(row.count('#') for row in board)
        return counter
    else:  # This counts in a proximity of one to the current index
        counter = 0
        # Check for all fields in radius
        for r in range(current_row - radius, current_row + radius + 1):
            for c in range(current_char - radius, current_char + radius + 1):
                if (r == current_row and c == current_char) or r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                    continue
                if board[r][c] == '#':
                    counter += 1
        return counter

field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")

