#!/usr/bin/env python3

def evolve(world, steps):
    pass

    """
    * A cell that is populated and has only one or no populated neighbors dies of solitude and becomes unpopulated.
    * A cell that is populated and has four or more populated neighbors dies due to overpopulation and becomes unpopulated.
    * A cell that is populated and has two or three populated neighbors survives and stays populated.
    * A cell that is unpopulated and has exactly three populated neighbor cells gets born and becomes populated.
    * All other cells remain unpopulated.
    * For cells next to the frame, frame cells are considered unpopulated from the cell's perspective.
    """

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

