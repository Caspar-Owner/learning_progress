tic_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nWelcome to Tic Tac Toe!\nThe board is numbered as follows:")

for row in tic_board:
    print(row[0], "|", row[1], "|", row[2])
    print("---------")
    # print(row)

while True:
    try:
        first_player = int(input("\nEnter the position for the first player (X): "))
        for row in tic_board:
            if first_player in row:
                row[row.index(first_player)] = 'X'
                
        for row in tic_board:
            if first_player in row :
                print("Position already taken. Please choose a different position.")
                continue

        for row in tic_board:
            print(row[0], "|", row[1], "|", row[2])
            print("---------")
            # print("fuck u")

        second_player = int(input("Enter the position for the second player (O): "))
        for row in tic_board:
            if second_player in row:
                row[row.index(second_player)] = 'O'

        for row in tic_board:
            if second_player in row :
                print("Position already taken. Please choose a different position.")
                continue

        for row in tic_board:
            print(row[0], "|", row[1], "|", row[2])
            print("---------")
            # print("fuck u")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue
    if tic_board[0][0] == tic_board[0][1] == tic_board[0][2] or \
       tic_board[1][0] == tic_board[1][1] == tic_board[1][2] or \
       tic_board[2][0] == tic_board[2][1] == tic_board[2][2] or \
       tic_board[0][0] == tic_board[1][0] == tic_board[2][0] or \
       tic_board[0][1] == tic_board[1][1] == tic_board[2][1] or \
       tic_board[0][2] == tic_board[1][2] == tic_board[2][2] or \
       tic_board[0][0] == tic_board[1][1] == tic_board[2][2] or \
       tic_board[0][2] == tic_board[1][1] == tic_board[2][0]:
        print("\nGame Over!")
        for row in tic_board:
            print(row[0], "|", row[1], "|", row[2])
            print("---------")
            # print("fuck u")
        break
