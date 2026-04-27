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

# Check full
def is_full(b):
    return ' ' not in b

# Exhaustive DFS (no scoring)
def exhaustive(b, player):
    if check_winner(b) or is_full(b):
        return

    for i in range(9):
        if b[i] == ' ':
            b[i] = player
            exhaustive(b, 'O' if player == 'X' else 'X')
            b[i] = ' '   # backtrack

# AI move (no optimization)
def ai_move():
    for i in range(9):
        if board[i] == ' ':
            temp = board.copy()
            temp[i] = 'X'
            exhaustive(temp, 'O')   # explore all states
            return i   # just pick first move

# Game start
print("TIC-TAC-TOE (EXHAUSTIVE SEARCH)")
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