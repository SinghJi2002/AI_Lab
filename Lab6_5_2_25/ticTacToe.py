import copy
import heapq

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X' 
        self.opponent = 'O'
        
    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def get_available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def make_move(self, row, col, player):
        self.board[row][col] = player


def bfs_search(game):
    queue = [(copy.deepcopy(game.board), [])]
    best_move = None

    while queue:
        state, moves = queue.pop(0)

        if TicTacToe().is_winner(game.current_player):
            return moves[0] if moves else None

        for move in game.get_available_moves():
            new_state = copy.deepcopy(state)
            new_state[move[0]][move[1]] = game.current_player
            queue.append((new_state, moves + [move]))

    return best_move  
def dfs_search(game):
    stack = [(copy.deepcopy(game.board), [])]
    best_move = None

    while stack:
        state, moves = stack.pop()

        if TicTacToe().is_winner(game.current_player):
            return moves[0] if moves else None

        for move in game.get_available_moves():
            new_state = copy.deepcopy(state)
            new_state[move[0]][move[1]] = game.current_player
            stack.append((new_state, moves + [move]))

    return best_move

def heuristic(state, player):
    game = TicTacToe()
    game.board = state

    if game.is_winner(player):
        return 1
    elif game.is_winner(game.opponent):
        return -1
    return 0

def a_star_search(game):
    priority_queue = []
    heapq.heappush(priority_queue, (0, [], copy.deepcopy(game.board)))

    while priority_queue:
        _, moves, state = heapq.heappop(priority_queue)

        if TicTacToe().is_winner(game.current_player):
            return moves[0] if moves else None

        for move in game.get_available_moves():
            new_state = copy.deepcopy(state)
            new_state[move[0]][move[1]] = game.current_player
            cost = len(moves) + heuristic(new_state, game.current_player)
            heapq.heappush(priority_queue, (cost, moves + [move], new_state))

    return None

def compare_algorithms():
    game = TicTacToe()

    bfs_move = bfs_search(game)
    print(f"BFS Selected Move: {bfs_move}")

    dfs_move = dfs_search(game)
    print(f"DFS Selected Move: {dfs_move}")

    astar_move = a_star_search(game)
    print(f"A* Selected Move: {astar_move}")

    if astar_move:
        game.make_move(astar_move[0], astar_move[1], game.current_player)
        print("Board after AI move using A*:")
        game.display_board()

compare_algorithms()
