class Cell:
    def __init__(self, x, y, traversable):
        self.x = x
        self.y = y
        self.traversable = traversable

def cell_decomposition(start, goal, grid):
    cells = [[Cell(x, y, grid[x][y] == 0) for y in range(len(grid[0]))] for x in range(len(grid))]
    
    # BFS to find path
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        
        if current == goal:
            return path
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < len(cells)) and (0 <= neighbor[1] < len(cells[0])) and cells[neighbor[0]][neighbor[1]].traversable and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []

# Example grid definition
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Example usage
start = (0, 0)
goal = (4, 4)
path = cell_decomposition(start, goal, grid)
print(f"Cell Decomposition path: {path}")
