from ast import Break
import time
import player 
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 
        self.current_winner = None 
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + " | ".join(row)+ " |")
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 | etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + " | ".join(row)+ " |")
    
    def available_moves(self):
        # for returing empty space 
        return [i for i,spot in enumerate(self.board) if spot == " "]

        # without list comprhenssion 
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ['x','x','o'] --> [(0,'x'), (1,'x'), (2,'o')]
        #     if spot == " ":
        #         moves.append(i)
        # return moves

    def is_empty_square(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return len(self.board)
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # checking winner on each move 
        # if any row is matching 
        row_index = square //3
        row = self.board[row_index: (row_index+1)*3]
        if all(spot == letter for spot in row):
            return True
        
        # checking column
        col_index = square %3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        # checking diagonal 
        if square%2 ==0 :
            diagonal1 = [self.board[i] for i in [0,4,8]] 
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagonal2):
                return True 
            
        return False
def play(game, x_player, o_player, print_game = True,sleep_time = 1):
    # returns the winner of the game(the letter) or None for a tie
    if print_game:
        game.print_board_nums()
     
    letter = 'x' # starting letter 
    
    # iterate till game has empty spot break the loop if either of them win 
    while game.is_empty_square():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square ({square})")
                game.print_board()
                print('')
            
            # check for winner 
            if game.current_winner == letter:
                if print_game:
                    print(f'{letter} won!')
                return letter
            letter = 'o' if letter =='x' else 'x'
        
        # add a pause just to pretend computer thinking 
        time.sleep(sleep_time)
    if print_game:
        print("It's a tie!")



if __name__ == "__main__":
    while True:
        x_win = 0
        o_win = 0
        tie = 0
        print("MENU")
        print("1. Play with computer\n2. Play with Smart computer\n3. Play with Human Player\n4. Verify Smart computer player\n5. Exit")
        choice  = int(input("Enter your choice : "))
        if 1>choice>5:
            print("Invalid choice Try again!")
        elif choice == 1:
            x_player = player.HumanPlayer('x')
            o_player = player.RandomComputerPlayer('o')
        elif choice == 2:
            x_player = player.HumanPlayer('x')
            o_player = player.GeniusComputerPlayer('o')
        elif choice == 3:
            x_player = player.HumanPlayer('x')
            o_player = player.HumanPlayer('o')
        elif choice == 4:
            n = 1000
            for _ in range(n):
                x_player = player.RandomComputerPlayer('x')
                o_player = player.GeniusComputerPlayer('o')
                t = TicTacToe()
                result = play(t,x_player,o_player,print_game=False,sleep_time=0)
                if result == "x":
                    x_win +=1
                elif result == "o":
                    o_win +=1
                else:
                    tie +=1
            print(f"Game Played {n} Game won {o_win} Game Lost {x_win} Ties {tie}")
            continue
        elif choice == 5:
            break
        t = TicTacToe()
        play(t,x_player,o_player,print_game=True,sleep_time=1)

