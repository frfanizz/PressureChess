import sys


'''

Considerations:
  allow buring pieces

'''



class tile:
  """
  (Board) tile objects
  """
  def __init__(self, piece, hp = 6):
    self.piece = piece
    self.hp = hp
  
  def lose_hp(self):
    self.hp = self.hp - 1 if self.hp > 0 else 0
  
  def get_piece(self):
    return self.piece
  
  def set_piece(self, piece):
    self.piece = piece
  
  def toString(self):
    if self.piece is None:
      return "  " + str(self.hp)
    else:
      return " " + self.piece.toString() + str(self.hp)

class board:
  """
  The chess board, which is an 8x8 array of tiles
  """
  def __init__(self, tiles):
    self.tiles = tiles
  
  # def is_in_check(self)
  
  def print_board(self):
    print(self.toString())
  
  def toString(self):
    retString = "\n  +---+---+---+---+---+---+---+---+\n"
    for row in range(len(self.tiles)-1, -1, -1):
      retString += str(row+1) + " "
      for tile in range(len(self.tiles[row])-1, -1, -1):
        retString += "|" + self.tiles[row][tile].toString() + ""
      retString += "|\n  +---+---+---+---+---+---+---+---+\n"
    retString += "    a   b   c   d   e   f   g   h  \n"
    return retString


class piece:
  """
  A chess piece
  """
  def __init__(self, side):
    self.side = side
  
  def can_move():
    pass
  def can_take():
    pass
  def move_take():
    pass

class position:
  """
  The position on the board, where rank = row (a : 0), and file = col (1 : 0)
  """
  def __init__(self, pos_rank, pos_file):
    self.pos_rank = pos_rank # row
    self.pos_file = pos_file # column
  
  def get_rank():
    return self.pos_rank
  
  def get_file():
    return self.pos_file
  
  def rank_to_string(self):
    return str(self.pos_rank + 1)
  
  def file_to_string(self):
    return chr(ord("a")+self.pos_file)

  def toString(self):
    return self.file_to_string() + self.rank_to_string()

class pawn:
  """
  A pawn
  """
  def __init__(self, side):
    self.side = side
  def toString(self):
    return "p"

class king:
  """
  A king
  """
  def __init__(self, side):
    self.side = side
  def toString(self):
    return "K"

class quee:
  """
  A queen
  """
  def __init__(self, side):
    self.side = side
  def toString(self):
    return "Q"

class bish:
  """
  A bishop
  """
  def __init__(self, side):
    self.side = side
  def toString(self):
    return "B"

class knig:
  """
  A knight
  """
  def __init__(self, side):
    self.side = side
  def toString(self):
    return "N"

class rook:
  """
  A rook
  """
  def __init__(self, side):
    self.side = side
  def toString(self):
    return "R"

  # def can_move(self, new_position):
  #   if self.position != new_position:
  #     if self.position.get_file() = new_position.get_file() or self.position.get_rank() = new_position.get_rank():
  #       return True
  #   return False

  # def can_take(self, new_position):
  #   if self.position != new_position:
  #     if self.position.get_file() = new_position.get_file() or self.position.get_rank() = new_position.get_rank():
  #       return True
  #   return False
  
  

'''

+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+

'''



board_std = [
              [tile(rook(0), 5), tile(knig(0), 5), tile(bish(0), 5), tile(quee(0), 5),
                      tile(king(0), 5), tile(bish(0), 5), tile(knig(0), 5), tile(rook(0), 5)],
              [tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5),
                      tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5)],
              [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
                      tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
              [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
                      tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
              [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
                      tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
              [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
                      tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
              [tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5),
                      tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5)],
              [tile(rook(1), 5), tile(knig(1), 5), tile(bish(1), 5), tile(quee(1), 5),
                      tile(king(1), 5), tile(bish(1), 5), tile(knig(1), 5), tile(rook(1), 5)]
]


# board_std = [
#               [tile(rook(0), 5), tile(rook(0), 5), tile(rook(0), 5), tile(rook(0), 5),
#                       tile(rook(0), 5), tile(rook(0), 5), tile(rook(0), 5), tile(rook(0), 5)],
#               [tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5),
#                       tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5), tile(pawn(0), 5)],
#               [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
#                       tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
#               [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
#                       tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
#               [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
#                       tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
#               [tile(None, 5), tile(None, 5), tile(None, 5), tile(None, 5),
#                       tile(None, 5), tile(None, 5),  tile(None, 5),  tile(None, 5)],
#               [tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5),
#                       tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5), tile(pawn(1), 5)],
#               [tile(rook(1), 5), tile(rook(1), 5), tile(rook(1), 5), tile(rook(1), 5),
#                       tile(rook(1), 5), tile(rook(1), 5), tile(rook(1), 5), tile(rook(1), 5)]
# ]


def main(argv):
  # f = open(argv[0], 'r+')
  
  # currLine = f.read()
  
  # while currLine != "" :
  #   # Do something with currLine
  #   print(currLine)
  #   # Read next line
  #   currLine = f.read()
  field = board(board_std)
  print(field.toString())

if __name__ == "__main__":
  main(sys.argv)
