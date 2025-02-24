import random

# Tic-Tac-Toe Board
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print("\n")

def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), 
                      (0,3,6), (1,4,7), (2,5,8), 
                      (0,4,8), (2,4,6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def ai_move():
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available_moves)
    board[move] = "O"

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner("X"):
            print("🎉 You win!")
            break
        if is_draw():
            print("😐 It's a draw!")
            break

        ai_move()
        print("\nAI's move:")
        print_board()
        if check_winner("O"):
            print("😞 AI wins!")
            break

if __name__ == "__main__":
    main()
