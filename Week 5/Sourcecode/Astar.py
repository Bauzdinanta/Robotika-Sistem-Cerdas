import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}

    # Inisialisasi g_score dan f_score untuk semua posisi di grid
    g_score = { (x, y): float('infinity') for x in range(len(grid)) for y in range(len(grid[0])) }
    g_score[start] = 0
    
    f_score = { (x, y): float('infinity') for x in range(len(grid)) for y in range(len(grid[0])) }
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        # Periksa semua tetangga yang mungkin
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Pastikan neighbor berada dalam batas grid dan bukan hambatan
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                
                # Jika jalur yang ditemukan lebih baik, perbarui
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    
                    # Tambahkan neighbor ke open_set jika belum ada
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = astar(start, goal, grid)
print(f"A* path: {path}")
