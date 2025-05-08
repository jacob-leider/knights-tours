#!/usr/bin/python3


import turtle
import random
from chess import *
from draw import *


def advance(pos, moves):
    """Move in a random direction, or quite frankly, don't move at all if you 
    can't """
    x, y = pos
    moves = list(good_moves(x, y, moves, visited))
    if len(moves) == 0: 
        return None

    dx, dy = random.choice(moves)
    x2, y2 = x + dx, y + dy

    if in_bounds(x2, y2) and (x2, y2) not in visited:
        visited.add((x2, y2))
        x, y = x2, y2
    
    return (x, y)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.tracer(0)

    n = 8 # board size is n x n
    side = 64

    # Grid.
    grid_turtle = turtle.Turtle()
    grid_turtle.hideturtle()
    grid_size =  side * n
    draw_grid(grid_turtle, grid_size, n)

    screen.update()
    
    # What the hell is even that
    mark_radius = 10
    pos = (0, 0)
    start = (0, 0)
    visited = {(0, 0)}

    # Move to center of bottom left cell
    t = turtle.Turtle()
    t.penup()
    diag = (n / 2 - 0.5) * side
    t.goto(-diag, -diag)
    t.pendown()

    # Find a path.
    while True:
        # Move in a random direction.
        next_pos = advance(pos, knight_moves())
        if next_pos is None:
            break

        # If we moved, draw the update.
        if pos != next_pos:
            draw_advance(t, pos, next_pos, side, mark_radius=mark_radius, pause=0.075)
            screen.update()

        pos = next_pos

    screen.mainloop()
