#!/usr/bin/python3


import turtle
from chess import *
from draw import *


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.tracer(0)

    n = 7 # board size is n x n
    side = 64

    # Grid.
    grid_turtle = turtle.Turtle()
    grid_turtle.hideturtle()
    grid_size = side * n
    draw_grid(grid_turtle, grid_size, n)

    screen.update()

    # Move to center of bottom left cell
    t = turtle.Turtle()
    t.penup()
    diag = (n / 2 - 0.5) * side
    t.goto(-diag, -diag)
    t.pendown()

    # Find a knight tour.
    start = (0, 0)
    moves = knight_moves()
    seq = find_hamiltonian_path(start, moves, bounds=(0,n,0,n))
    if seq is None:
        raise Exception("No hamiltonian path found.")

    for i in range(1, len(seq)):
        pos = seq[i - 1]
        next_pos = seq[i]
        draw_advance(t, pos, next_pos, side, mark_radius=10, pause=0.075)
        screen.update()

    screen.mainloop()
