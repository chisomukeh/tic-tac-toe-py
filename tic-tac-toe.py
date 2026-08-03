from math import inf
from random import choice

board = ["", "", "", "", "", "", "", "", ""]
win_combination = [
    # horizontal
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    
    # vertical
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    
    # diagonal
    [0, 4, 8], [2, 4, 6]
]


def print_board(board):
    print("[TIC TAC TOE]\n+---+---+---+")
    row = "|"
    for i in range(len(board)):
        if board[i]:
            row += " " + board[i] + " |"
        else:
            row += "   |"
            
        if (i + 1) % 3 == 0:
            print(row)
            print("+---+---+---+")
            row = "|"
    

def get_avaliable_moves(board):
    return [i for i, spot in enumerate(board) if spot == ""]


def has_won(board, player):
    for combo in win_combination:
        a, b, c = combo
        if board[a] == player and board[b] == player and board[c] == player:
            return True
            
    return False
    

# AI
# minimax algorithm
def get_best_move(board, depth, max_depth, maximizing):
    if depth == max_depth or has_won(board, "X") or has_won(board, "O") or len(get_avaliable_moves(board)) == 0:
        if has_won(board, "X"):
            return 100 - depth
        elif has_won(board, "O"):
            return -100 + depth
        else:
            return 0
            
    node = {}
            
    if maximizing:
        value = -inf
        for m in get_avaliable_moves(board):
            clone_board = board.copy()
            clone_board[m] = "X"
            
            node_value = get_best_move(clone_board, depth + 1, max_depth, False)
            value = max(value, node_value)
            
            if depth == 0:
                node.setdefault(node_value, []).append(m)
                
        if depth == 0:
            return choice(node[value])
                
        return value
                
    else:
        value = inf
        for m in get_avaliable_moves(board):
            clone_board = board.copy()
            clone_board[m] = "O"
            
            node_value = get_best_move(clone_board, depth + 1, max_depth, True)
            value = min(value, node_value)
            
            if depth == 0:
                node.setdefault(node_value, []).append(m)
                    
        if depth == 0:
            return choice(node[value])
        
        return value
        

# AI vs AI
def play(max_depth):
    while True:
        best = get_best_move(board, 0, max_depth, True)
        board[best] = "X"
        print_board(board)
        print("best: " + str(best) + "\n")
        
        if has_won(board, "X"):
        	print("Game Over: X is winner")
        	return
        	
        if len(get_avaliable_moves(board)) == 0:
        	break
        	
        best = get_best_move(board, 0, max_depth, False)
        board[best] = "O"
        print_board(board)
        print("best: " + str(best) + "\n")
        
        if has_won(board, "O"):
        	print("Game Over: O is winner")
        	return
        
    print("Game Over: it's a draw")

    