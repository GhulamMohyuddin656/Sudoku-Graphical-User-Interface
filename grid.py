# grid.py
import os
def read_sudoku(difficulty,number):
    filename=f"{difficulty.lower()}_puzzle{number}.txt"
    base_dir=os.path.dirname(__file__)
    full_path=os.path.join(base_dir,"Puzzles",filename)
    if os.path.exists(full_path):
        grid = []
        with open(full_path, 'r') as file:
            for line in file:
                grid.append([int(ch) for ch in line.strip()])
        return grid
    else:
        return None

def print_grid(grid_dict):
    for r in range(9):
        row = []
        for c in range(9):
            row.append(str(grid_dict[(r,c)]))
        print(" ".join(row))


def build_constraints():
    constraints = {}

    for r in range(9):
        for c in range(9):
            neighbors = set()

            for i in range(9):
                neighbors.add((r, i))
                neighbors.add((i, c))

            br = (r // 3) * 3
            bc = (c // 3) * 3

            for i in range(3):
                for j in range(3):
                    neighbors.add((br+i, bc+j))

            neighbors.remove((r,c))
            constraints[(r,c)] = neighbors

    return constraints

def Setup_CSP(grid):
    domains = {}
    assignment = {}

    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                domains[(r,c)] = [1,2,3,4,5,6,7,8,9]
            else:
                domains[(r,c)] = [grid[r][c]]
                assignment[(r,c)] = grid[r][c]

    constraints = build_constraints()
    return domains,assignment,constraints