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
  
  