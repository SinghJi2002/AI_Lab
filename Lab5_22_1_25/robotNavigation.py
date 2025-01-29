import heapq
import math
import matplotlib.pyplot as plt
import numpy as np

class GridSearch:
    def __init__(self, grid, start, goal, allow_diagonal=False):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.allow_diagonal = allow_diagonal

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 1

    def get_neighbors(self, x, y):
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)  
        ]
        if self.allow_diagonal:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
        neighbors = [(x + dx, y + dy) for dx, dy in directions if self.is_valid(x + dx, y + dy)]
        return neighbors

    def manhattan_distance(self, x, y):
        return abs(self.goal[0] - x) + abs(self.goal[1] - y)

    def euclidean_distance(self, x, y):
        return math.sqrt((self.goal[0] - x) ** 2 + (self.goal[1] - y) ** 2)

    def a_star(self, heuristic="manhattan"):
        h = self.manhattan_distance if heuristic == "manhattan" else self.euclidean_distance

        
        priority_queue = []
        heapq.heappush(priority_queue, (0, 0, self.start, [self.start]))
        visited = set()

        while priority_queue:
            f, g, (x, y), path = heapq.heappop(priority_queue)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == self.goal:
                return path

            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) not in visited:
                    new_g = g + 1
                    new_f = new_g + h(nx, ny)
                    heapq.heappush(priority_queue, (new_f, new_g, (nx, ny), path + [(nx, ny)]))

        return None 

    def bfs(self):
        queue = [(self.start, [self.start])]
        visited = set()

        while queue:
            (x, y), path = queue.pop(0)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == self.goal:
                return path

            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))

        return None 

    def uniform_cost_search(self):
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.start, [self.start]))
        visited = set()

        while priority_queue:
            cost, (x, y), path = heapq.heappop(priority_queue)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == self.goal:
                return path

            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) not in visited:
                    heapq.heappush(priority_queue, (cost + 1, (nx, ny), path + [(nx, ny)]))

        return None

def plot_path(grid, path, title):
    grid = np.array(grid)
    for x, y in path:
        grid[x][y] = 0.5  

    plt.imshow(grid, cmap="Greys", origin="upper")
    plt.title(title)
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.colorbar(label="Cell Values")
    plt.show()

grid = [
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

start = (0, 0)
goal = (4, 4)

grid_search = GridSearch(grid, start, goal, allow_diagonal=True)

path_manhattan = grid_search.a_star(heuristic="manhattan")
plot_path(grid, path_manhattan, "A* (Manhattan Distance)")

path_euclidean = grid_search.a_star(heuristic="euclidean")
plot_path(grid, path_euclidean, "A* (Euclidean Distance)")

path_bfs = grid_search.bfs()
plot_path(grid, path_bfs, "BFS")

path_ucs = grid_search.uniform_cost_search()
plot_path(grid, path_ucs, "Uniform Cost Search")
