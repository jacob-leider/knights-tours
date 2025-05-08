#!/usr/bin/python3


def knight_moves():
    """Which directions can I move in euclidean coordinates?"""
    return ((+2, +1), (+1, +2), (-1, +2), (-2, +1),
            (-2, -1), (-1, -2), (+1, -2), (+2, -1))


def in_bounds(x, y, bounds=(0, 8, 0, 8)):
    """Are we still on the board?"""
    xmin, xmax, ymin, ymax = bounds
    return xmin <= x < xmax and ymin <= y < ymax



def all_neighbors(pos, moves, bounds=(0, 8, 0, 8)):
    """Where can I go?"""
    x, y = pos
    for dx, dy in moves:
        if in_bounds(x + dx, y + dy, bounds=bounds):
            yield (x + dx, y + dy)


def good_neighbors(x, y, moves, visited, bounds=(0, 8, 0, 8)):
    """Where can I go that I haven't yet been?"""
    for dx, dy in moves:
        if in_bounds(x + dx, y + dy, bounds=bounds) and (x + dx, y + dy) not in visited:
            yield (x + dx, y + dy)


def good_moves(x, y, moves, visited, bounds=(0, 8, 0, 8)):
    """Where can I go that I haven't yet been?"""
    for dx, dy in moves:
        if in_bounds(x + dx, y + dy, bounds=bounds) and (x + dx, y + dy) not in visited:
            yield (dx, dy)


def find_hamiltonian_path(start, moves, maxnodes=1000000, bounds=(0,8,0,8)):
    stack = []
    xmin, xmax, ymin, ymax = bounds
    n = xmax * ymax

    # Try starting from each node
    stack.append((start, [start], set([start])))

    while stack:
        curr, path, visited = stack.pop()

        if len(path) == n:
            return path  # Hamiltonian path found

        for neighbor in all_neighbors(curr, moves, bounds=bounds):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor], visited | {neighbor}))

    return None  # No Hamiltonian path found   
