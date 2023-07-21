import time
def plot_movement(movements):
    x, y = 0, 0
    grid = {(x, y): 'o'}  # Mark starting position with 'o'

    for direction in movements:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        grid[(x, y)] = 'x'  # Mark new position with 'x'

    # Find the bounds of the grid
    min_x = min(x for x, y in grid.keys())
    max_x = max(x for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    # Print the grid
    for j in range(max_y, min_y - 1, -1):
        for i in range(min_x, max_x + 1):
            print(grid.get((i, j), '.'), end=' ')
        print()
        time.sleep(1)

# Example movements
movements = "NNNEESSW"
plot_movement(movements)