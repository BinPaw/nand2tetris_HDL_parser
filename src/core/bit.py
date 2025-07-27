class Bit:
  def __init__(self, val: bool = False) -> None:
    self.val = val

  def Nand(self, a: bool, b: bool) -> None:
    self.val = not (a and b)

  def Not(self, a: bool) -> None:
    self.val = not a

  def And(self, a: bool, b: bool) -> None:
    self.val = a and b

  def Or(self, a: bool, b: bool) -> None:
    self.val = a or b