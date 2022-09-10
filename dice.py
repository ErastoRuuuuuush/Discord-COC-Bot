######################################
# The core driver for rolling dice.
# 
# Maintaince Member:
#   Eric Liu
######################################
import random

ERROR = 0
FAIR = 1
DRAMA = 2 # Not implemented

class Dice:
  """
  Dice is a dice that can be rolled to return a number.
  
  Fields:
    min  Minimum value of a dice
    max  Maximum value of a dice
    type Determine the fair type of the dice
  """
  
  def __init__(self, min=1, max=100, type=FAIR):
    self.min = min
    self.max = max
    self.type = type
    return

  # Returns a random Int, with value >= min and <= max
  def rowDice(self):
    type = self.type
    if type == FAIR:
      return random.randint(self.min, self.max)
    else:
      return ERROR
