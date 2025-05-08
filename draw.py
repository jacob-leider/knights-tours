#!/usr/bin/python3


import time
import math


def draw_square_on_cursor(t, radius):
    """Draws a square centered at the turtle."""
    # Go away
    t.penup()
    t.setheading(225)
    t.fd(radius / 2**1.5)

    # Draw the square
    t.begin_fill()
    t.setheading(0)
    for _ in range(4):
        t.forward(radius) # Move forward 100 units
        t.left(90)   # Turn left 90 degrees
    t.end_fill()

    # Come back
    t.setheading(45)
    t.fd(radius /  2**1.5)
    t.pendown()


def draw_grid(turtle, size, divisions):
    """Draws a grid using the turtle."""
    cell_size = size / divisions
    for i in range(divisions + 1):
        # Draw horizontal lines
        turtle.penup()
        turtle.goto(-size / 2, size / 2 - i * cell_size)
        turtle.pendown()
        turtle.forward(size)

        # Draw vertical lines
        turtle.penup()
        turtle.goto(-size / 2 + i * cell_size, size / 2)
        turtle.pendown()
        turtle.setheading(270)  # Point downwards
        turtle.forward(size)
        turtle.setheading(0)  # Reset to original direction


def draw_advance(t, pos, pos2, dist, mark_radius=10, pause=0.0):
    """Move in a random direction, or quite frankly, don't move at all if you 
    can't """
    x1, y1 = pos
    x2, y2 = pos2
    r = dist * 5**0.5
    dx, dy = x2 - x1, y2 - y1

    # Cartesian to polar.
    theta = math.degrees(math.atan(dy / dx))
    if dx < 0:
        theta += 180

    # Go forth.
    t.setheading(theta)
    t.fd(r)
    
    draw_square_on_cursor(t, mark_radius)

    # Pause.
    time.sleep(pause)
