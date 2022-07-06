from lib2to3.pgen2.literals import simple_escapes
import random 
import game
import math 

class Player:
    def __init__(self, letter):
        self.letter = letter 

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        # get any random move from valid move list 
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_move = False
        val = None
        while not valid_move:
            square = input(f"{self.letter}'s turn, Enter your move(0-8) : ")
            # id value isn't numerical or out of the range 0-9 or any invalid move we will give and invalid move message 
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print(' Invalid move. Try again!')
        
        return val

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves)
        else:
            square = self.minmax(game, self.letter)['position']
        return square
    
    def minmax(self, state, player): # state-> current state of game 
        max_player = self.letter
        other_player = 'o' if player== 'x' else 'x'

        # first, we want to check if the previous move is a winner
        # this is our base case  
        if state.current_winner == other_player:
            # returns score->to keep track of position and position also
            return {'position' : None,
            'score' : 1*(state.num_empty_square()+1) if other_player == max_player else -1*(state.num_empty_square()+1) }

        elif not state.is_empty_square():
            return {'position':None, 'score':0}
        
        if player == max_player:
            best = {'position':None, 'score':-math.inf}
        else :
             best = {'position':None, 'score': math.inf}
        
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot 
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simmulate a game after making that move 
            sim_score = self.minmax(state, other_player)

            # step3: undo everything 
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if necessary 
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best




