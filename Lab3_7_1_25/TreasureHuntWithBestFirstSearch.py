import heapq

def manhattan_distance(x, y, goal_x, goal_y):
    """Calculate the Manhattan distance."""
    return abs(goal_x - x) + abs(goal_y - y)

def best_first_search(grid, start, goal):
    """Best-First Search to locate the treasure."""
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = start
    goal_x, goal_y = goal
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()
    nodes_explored = 0

    while priority_queue:
        heuristic, (x, y), path = heapq.heappop(priority_queue)
        nodes_explored += 1

        if (x, y) == goal:
            return path, nodes_explored
        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                heuristic = manhattan_distance(nx, ny, goal_x, goal_y)
                heapq.heappush(priority_queue, (heuristic, (nx, ny), path + [(nx, ny)]))

    return None, nodes_explored

grid = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

start = (0, 0)  # Starting position
goal = (3, 3)   # Treasure location

path, nodes_explored = best_first_search(grid, start, goal)
print("Path to Treasure:", path)
print("Nodes Explored:", nodes_explored)

