"""
Tic-Tac-Toe with an unbeatable AI (minimax algorithm).
"""

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(" | ".join(str(c) for c in row))
        if i < 6:
            print("--+---+--")
    print()


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def minimax(board, is_maximizing):
    win = winner(board)
    if win == AI:
        return 1
    if win == HUMAN:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best = min(best, score)
        return best


def best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move


def main():
    board = [EMPTY] * 9
    print("Tic-Tac-Toe: you are X, AI is O. Positions are numbered 0-8, left to right, top to bottom.")
    print_board(list(range(9)))

    while True:
        # Human turn
        while True:
            try:
                move = int(input("Your move (0-8): "))
                if 0 <= move <= 8 and board[move] == EMPTY:
                    break
                print("Invalid move, try again.")
            except ValueError:
                print("Enter a number from 0 to 8.")
        board[move] = HUMAN
        print_board(board)

        if winner(board) == HUMAN:
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI turn
        ai_move = best_move(board)
        board[ai_move] = AI
        print(f"AI plays {ai_move}.")
        print_board(board)

        if winner(board) == AI:
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
