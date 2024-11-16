#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    game_state_check(state)
    move_check(state, direction)

    # actual move
    new_bord = actual_move(state, direction)
    new_moves = move_check(new_bord)

    new_bord = (''.join(row) for row in new_bord)

    return (new_bord, new_moves)

def move_check(state, direction = None):    # Check if the move is even possible or if the provided direction is not in the possible move list

    x, y = character_finder(state)          # Find the idx of player character
    
    move_list=possible_moves(state, (x, y)) # Creates a movelist, but if movelist is empty raises a warning

    if direction == None:                   # returns the move_list
        return move_list
    
    if direction != None:
        if direction not in move_list:      # Check if there is a move that is possible
            raise Warning("The move is not possible")
    
def game_state_check(state):                # Check if the bord is valid

    # Test_methods for clean code
    bord_dimension_checker(state)
    one_character_check(state)

def one_character_check(state):             # Check if there is a character on the bord and only one and if the characters on the bord are valid

    counter = 0
    for row in state:
        for character in list(row):
            if character not in (" ", "#", "o"):
                raise Warning(f"invalid character: {character}")            # test_invalid_bord_character(self):
            if character == "o":
                counter += 1
    
    if counter == 0:
        raise Warning("no player character found")                          # test_no_player_character(self):
    
    if counter > 1:
        raise Warning("too many players")                                   # test_too_many_players(self):

def bord_dimension_checker(state):          # Check if the bord has the right dimensions
    
    if len(state) == 0:                     # Check if the state has no rows
        raise Warning("The bord is too small.")
    
    for row in state:                       
        if len(state[0]) != len(row):       # Check if each line has same length.
            raise Warning("The bord has different row dimensions")
        if len(row) == 0:                   # Check if the rowlength is 0
            raise Warning("The bord is too small")

def character_finder(state):                # find the idx of player character

    for y in range(len(state)):
        row = list(state[y])

        for x in range(len(row)):
            if row[x] == 'o':
                return x, y

def possible_moves(state, player_idx):      # Returns a list of all the possible moves at the player character
    move_list = []
    x, y = player_idx

    if list(state[y+1])[x] == ' ':        # Check if one idx down is ' '
        move_list.append("down")

    if list(state[y])[x-1] == ' ':        # Check if one idx left is ' '
        move_list.append("left")

    if list(state[y])[x+1] == ' ':        # Check if one idx right is ' '
        move_list.append("right")

    if list(state[y-1])[x] == ' ':        # Check if one idx up is ' '
        move_list.append("up")

    if move_list == []:
        raise Warning("There are no possible moves")
    
    return tuple(move_list)

def actual_move(state, direction):          # Brain of the move
    
    idx_player = character_finder(state)    # identidy the player index
    idx_move = move_idx(idx_player, direction)   # identify the move index

    return swapper(state, idx_player, idx_move)

def move_idx(idx_player, direction):        # Takes old position of player and adds the direction to x y
    x, y = idx_player

    if direction == "down":
        return x, y+1
        
    elif direction == "left":
        return x-1, y
    
    elif direction == "right":
        return x+1, y
        
    elif direction == "up":
        return x, y-1

def swapper(original, old_idx, new_player): # Swaps the old char with ' ' and new location with 'o'
    ox, oy = old_idx
    nx, ny = new_player

    new_bord = []

    for row in range(len(original)):
        new_row = []
        row_list = list(original[row])              # right here......... 
        for char in range(len(original[row])):      # idxing
            if row == oy and char == ox:            # old char
                new_row.append(' ')
            elif row == ny and char == nx:
                new_row.append('o')
            else:
                new_row.append(row_list[char])
        new_bord.append(new_row)

    return new_bord

# Check if the move you want to make is possible
# Rocks "#" or lines are not possible to move to, only ' ', so maybe just check for the ' ' instead of everything else. 

# check whether this move is possible and, if yes, return the mutated game state, 
# as well as all possible walking directions in the new state, ordered alphabetically (i.e., `down` < `left` < `right` < `up`).


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
s2 = move(s1, "right")

print("= New State =")
print("\n".join(s2[0]))
print(f"\nPossible Moves: {s2[1]}")
