import os

LOGO = """
  __  .__        __                 __                 
_/  |_|__| _____/  |______    _____/  |_  ____   ____  
\   __\  |/ ___\   __\__  \ _/ ___\   __\/  _ \_/ __ \ 
 |  | |  \  \___|  |  / __ \\\\  \___|  | (  <_> )  ___/ 
 |__| |__|\___  >__| (____  /\___  >__|  \____/ \___  >
              \/          \/     \/                 \/ 
              """


def main():
    board_text = UserPlays()
    # take inputs in turns
    print(LOGO)
    player_1 = True
    counter = 0
    while True:
        show_board(board_text)
        if player_1:
            single = take_play("Player X", board_text)
        else:
            single = take_play("Player O", board_text)

        board_text.take_input(single, player_1)
        player_1 = not player_1

        # the command to clear is `cls` on Windows and `clear` on most everything else
        os.system('cls' if os.name == 'nt' else 'clear')
        print(LOGO)
        counter += 1

        # calculate if won
        winner = board_text.is_there_winner()
        if winner or counter >= 9:
            break


    # end game if won and print winner name
    show_board(board_text)
    if winner:
        print(f"Player {winner} has won!")
    else:
        print("Its a draw!")


# create a class to store max of 9 inputs
class UserPlays():
    def __init__(self):
        self.plays = [[" " for j in range(3)] for k in range(3)]

    def take_input(self, coordinates, player_1):
        if player_1:
            self.plays[coordinates[0]][coordinates[1]] = "X"
        else:
            self.plays[coordinates[0]][coordinates[1]] = "O"

    def not_played(self, coord1, coord2):
        if self.plays[coord1][coord2] == " ":
            return True
        else:
            return False

    def is_there_winner(self):
        # Check horizontal victories
        for i in range(3):
            each_row = list(set(self.plays[i]))
            if len(each_row) == 1 and each_row[0] != " ":
                return each_row[0]

        # check vertical victories
        for j in range(3):
            each_row = list(set([self.plays[k][j] for k in range(3)]))
            if len(each_row) == 1 and each_row[0] != " ":
                return each_row[0]

        # check diagonal victories
        each_row = list(set([self.plays[l][l] for l in range(3)]))
        if len(each_row) == 1 and each_row[0] != " ":
            return each_row[0]

        each_row = list(set([self.plays[ (l+1) *-1 ][l] for l in range(3)]))
        if len(each_row) == 1 and each_row[0] != " ":
            return each_row[0]

        return False

# print the empty tictac board
# allow the board to display the inputs stored in the class
def show_board(userplays: UserPlays):
    """Shows the board in the console"""
    for i in range(3):
        for j in range(3):
            print(userplays.plays[i][j], end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print('-' * 5)


# take inputs that show the coordinates of the board
def take_play(player: str, board: UserPlays):
    while True:
        single_input = input(f"{player}: Enter the play in the format row.col, eg. 3.2 for the bottom middle location "
                             "(Only the first 2 digits will be taken)\n").split(".")
        try:
            coord_1 = int(single_input[0]) - 1
            coord_2 = int(single_input[1]) - 1
        except (ValueError, IndexError):
            print("The input wasnt valid, please try again. ")
        else:
            if (0 <= coord_1 <= 2) and (0 <= coord_2 <= 2):
                if board.not_played(coord_1, coord_2):
                    break
                else:
                    print("That has already been played")
            else:
                print("The input wasnt valid, please try again. ")

    return coord_1, coord_2


if __name__ == "__main__":
    main()
