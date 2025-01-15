from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def neighbors(self, node):
        return self.graph.get(node, [])
    
def bidirectional_bfs(graph, start, end):
    if start == end:
        return [start], 0

    frontier_start = deque([start])
    frontier_end = deque([end])
    visited_start = {start: None}
    visited_end = {end: None}

    nodes_explored = 0

    while frontier_start and frontier_end:
        path = _expand_frontier(frontier_start, visited_start, visited_end, graph)
        nodes_explored += 1
        if path:
            return path, nodes_explored

        path = _expand_frontier(frontier_end, visited_end, visited_start, graph)
        nodes_explored += 1
        if path:
            return path, nodes_explored

    return None, nodes_explored  

def _expand_frontier(frontier, visited_this_side, visited_other_side, graph):
    current = frontier.popleft()
    for neighbor in graph.neighbors(current):
        if neighbor not in visited_this_side:
            visited_this_side[neighbor] = current
            frontier.append(neighbor)
            if neighbor in visited_other_side:  
                return _construct_path(neighbor, visited_this_side, visited_other_side)
    return None

def _construct_path(meeting_point, visited_start, visited_end):
    path_start = []
    current = meeting_point
    while current:
        path_start.append(current)
        current = visited_start[current]
    path_start.reverse()

    path_end = []
    current = visited_end[meeting_point]
    while current:
        path_end.append(current)
        current = visited_end[current]

    return path_start + path_end

def bfs(graph, start, end):
    if start == end:
        return [start], 0

    queue = deque([(start, [start])])
    visited = set()
    nodes_explored = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored += 1

        if current == end:
            return path, nodes_explored

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_explored

def dfs(graph, start, end):
    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        current, path = stack.pop()
        nodes_explored += 1

        if current == end:
            return path, nodes_explored

        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored

def compare_algorithms(graph, start, end):
    print("Running Bi-Directional BFS...")
    path_bi, explored_bi = bidirectional_bfs(graph, start, end)
    print(f"Path: {path_bi}, Nodes Explored: {explored_bi}")

    print("\nRunning Standard BFS...")
    path_bfs, explored_bfs = bfs(graph, start, end)
    print(f"Path: {path_bfs}, Nodes Explored: {explored_bfs}")

    print("\nRunning DFS...")
    path_dfs, explored_dfs = dfs(graph, start, end)
    print(f"Path: {path_dfs}, Nodes Explored: {explored_dfs}")

city_map = Graph()
edges = [
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"),
    ("D", "F"), ("E", "F"), ("F", "G"), ("B", "H")
]

for u, v in edges:
    city_map.add_edge(u, v)

start = "A"
end = "G"

compare_algorithms(city_map, start, end)


