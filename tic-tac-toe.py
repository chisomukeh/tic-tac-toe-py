import math
import random

board = ["", "", "", "", "", "", "", "", ""]
win_combination = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_board(board):
    print("[TIC TAC TOE]")
    print("+---+---+---+")
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
            
    print("")

def get_avaliable_moves(board):
    return [i for i, spot in enumerate(board) if spot == ""]

def has_won(board, player):
    for combo in win_combination:
        a, b, c = combo
        if board[a] == player and board[b] == player and board[c] == player:
            return True
            
    return False

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
        value = -math.inf
        for m in get_avaliable_moves(board):
            clone_board = board[:]
            clone_board[m] = "X"
            
            node_value = get_best_move(clone_board, depth + 1, max_depth, False)
            value = max(value, node_value)
            
            if depth == 0:
                node.setdefault(node_value, []).append(m)
                
        if depth == 0:
            return random.choice(node[value])
                
        return value
                
    else:
        value = math.inf
        for m in get_avaliable_moves(board):
            clone_board = board[:]
            clone_board[m] = "O"
            
            node_value = get_best_move(clone_board, depth + 1, max_depth, True)
            value = min(value, node_value)
            
            if depth == 0:
                node.setdefault(node_value, []).append(m)
                    
        if depth == 0:
            return random.choice(node[value])
        
        return value

def play(max_depth):
    while not has_won(board, "X") and not has_won(board, "O") and len(get_avaliable_moves(board)) > 0:
        board[get_best_move(board, 0, max_depth, True)] = "X"
        
        if has_won(board, "X"):
        	print_board(board)
        	print("Game Over: X is winner")
        	return
        	
        board[get_best_move(board, 0, max_depth, False)] = "O"
        
        if has_won(board, "O"):
        	print_board(board)
        	print("Game Over: O is winner")
        	return
        	
        print_board(board)
        
    print("Game Over: it's a draw")
