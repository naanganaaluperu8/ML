# Initialize board
board = [' '] * 9

# Print board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")
    print()

# Check winner
def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b1,c in wins:
        if b[a] == b[b1] == b[c] and b[a] != ' ':
            return b[a]
    return None

# Check draw
def is_full(b):
    return ' ' not in b

# Minimax function
def minimax(b, is_max):
    winner = check_winner(b)

    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_full(b):
        return 0

    if is_max:  # AI turn
        best = -999
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, False)
                b[i] = ' '
                best = max(best, score)
        return best
    else:  # Human turn
        best = 999
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, True)
                b[i] = ' '
                best = min(best, score)
        return best

# AI move
def ai_move():
    best_score = -999
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    return move

# Game start
print("TIC-TAC-TOE (MINIMAX)")
print("AI = X | Human = O")
print("Positions:\n0 1 2\n3 4 5\n6 7 8\n")

print_board()

while True:
    # AI move
    m = ai_move()
    board[m] = 'X'
    print("AI played:", m)
    print_board()

    if check_winner(board):
        print("Winner:", check_winner(board))
        break
    if is_full(board):
        print("Draw")
        break

    # Human move
    pos = int(input("Enter your move (0-8): "))
    if board[pos] != ' ':
        print("Invalid move")
        continue

    board[pos] = 'O'
    print_board()

    if check_winner(board):
        print("Winner:", check_winner(board))
        break
    if is_full(board):
        print("Draw")
        break