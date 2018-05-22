import sys
from pieces import *

'''
Considerations:
  allow buring pieces
'''


class tile:
  """
  (Board) tile objects
  """
  def __init__(self, piece, hp = 6):
    """
    Tile classs constructor

    :param self tile: the current object
    :param piece piece: the current object
    :param hp int: the current object
    """
    self.piece = piece
    self.hp = hp
  
  def lose_hp(self):
    """
    Decrements self's hp

    :param self tile: the current object
    :returns boolean: True if hp was decremented, False o.w.
    """
    if self.hp > 0:
      self.hp = self.hp - 1
      return True
    else:
      # self.hp = 0
      return False
  
  def get_piece(self):
    """
    Returns self's piece

    :param self tile: the current object
    :returns piece: the piece of the current object
    """
    return self.piece
  
  def set_piece(self, piece):
    """
    Sets self's piece to piece

    :param self tile: the current object
    :param piece piece: a piece object
    :returns:
    """
    self.piece = piece
  
  def toString(self):
    """
    Returns a string representation of self

    :param self tile: the current object
    :returns str: a string representation of self
    """
    if self.piece is None:
      return "  " + str(self.hp)
    else:
      return " " + self.piece.toString() + str(self.hp)

class board:
  """
  The chess board, which is an 8x8 array of tiles
  """
  def __init__(self, tiles):
    """
    Board class constructor

    :param self board: the current object
    :param tiles [tile]: an array of tiles
    :returns:
    """
    self.tiles = tiles
    # TODO: add curr player to move??
  
  # TODO: def is_in_check(self)
  
  def print_board(self):
    """
    Prints the board in a visually athstetic way

    :param self board: the current object
    :returns:
    """
    print(self.toString())
  
  def toString(self):
    """
    Returns a string representation of the board in a visually athstetic way

    :param self board: the current object
    :returns str: The board in a string representation
    """
    retString = "\n  +---+---+---+---+---+---+---+---+\n"
    for row in range(len(self.tiles)-1, -1, -1):
      retString += str(row+1) + " "
      for tile in range(len(self.tiles[row])):
        retString += "|" + self.tiles[row][tile].toString() + ""
      retString += "|\n  +---+---+---+---+---+---+---+---+\n"
    retString += "    a   b   c   d   e   f   g   h  \n"
    return retString




class position:
  """
  The position on the board, where rank = row (1 : 0), and file = col (a : 0)
  """
  def __init__(self, pos_rank, pos_file):
    """
    Position class constructor

    :param self position: the current object
    :param pos_rank int: the rank (row) number from 0 to 7
    :param pos_file int: the file (colum) number from 0 to 7
    :returns:
    """
    self.pos_rank = pos_rank # row
    self.pos_file = pos_file # column
  
  def get_rank(self):
    """
    Return self's rank

    :param self position: the current object
    :returns int: self's rank
    """
    return self.pos_rank
  
  def get_file(self):
    """
    Return self's file

    :param self position: the current object
    :returns int: self's file
    """
    return self.pos_file
  
  def rank_to_string(self):
    """
    Return self's rank in a string format from 1 to 8

    :param self position: the current object
    :returns str: self's rank in a string format
    """
    return str(self.pos_rank + 1)
  
  def file_to_string(self):
    """
    Return self's rank in a string format from a to h

    :param self position: the current object
    :returns str: self's rank in a string format
    """
    return chr(ord("a")+self.pos_file)

  def toString(self):
    """
    Return self in a string format (file followed by row)

    :param self position: the current object
    :returns str: self in a string format
    """
    return self.file_to_string() + self.rank_to_string()


board_std = [
              [tile(rook(0)), tile(knig(0)), tile(bish(0)), tile(quee(0)),
                      tile(king(0)), tile(bish(0)), tile(knig(0)), tile(rook(0))],
              [tile(pawn(0)), tile(pawn(0)), tile(pawn(0)), tile(pawn(0)),
                      tile(pawn(0)), tile(pawn(0)), tile(pawn(0)), tile(pawn(0))],
              [tile(None), tile(None), tile(None), tile(None),
                      tile(None), tile(None),  tile(None),  tile(None)],
              [tile(None), tile(None), tile(None), tile(None),
                      tile(None), tile(None),  tile(None),  tile(None)],
              [tile(None), tile(None), tile(None), tile(None),
                      tile(None), tile(None),  tile(None),  tile(None)],
              [tile(None), tile(None), tile(None), tile(None),
                      tile(None), tile(None),  tile(None),  tile(None)],
              [tile(pawn(1)), tile(pawn(1)), tile(pawn(1)), tile(pawn(1)),
                      tile(pawn(1)), tile(pawn(1)), tile(pawn(1)), tile(pawn(1))],
              [tile(rook(1)), tile(knig(1)), tile(bish(1)), tile(quee(1)),
                      tile(king(1)), tile(bish(1)), tile(knig(1)), tile(rook(1))]
]


def main(argv):
    """
    Main application class

    :param argv [str]: the terminal/command line inputs
    :returns:
    """
  field = board(board_std)
  print(field.toString())

if __name__ == "__main__":
  main(sys.argv)
