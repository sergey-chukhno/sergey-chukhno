import math 
import random 

class Player:
  def __init__(self, letter):
    # la lettre x ou o choisi par un joueur
    self.letter = letter

  #le coup de chacun des joueurs
  def get_move(self, game): 
    pass

class ComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    square = random.choice(game.available_moves()) #On utilise random.choice pour que l'ordinateur choisie au hasard un case disponible
    return square  

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square: 
      square = input(self.letter + '\s turn. Input move (0-9):')
      # On va s'assurer que la valeur introduite par le joueur est un int et que la case choisie est libre
      try: 
        val=int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True
      except ValueError:
        print('Invalid square. Please try again.')
    return val
  
 
