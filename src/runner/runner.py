from src.core.bit import Bit
from src.infra.reader import Reader

class Runner:
  def __init__(self, reader: Reader) -> None:
    self.reader = reader

  def run(self, parts: list[dict[str, str | dict[str, str]]], vars: dict[str, Bit]) -> None:
    vars['0'] = Bit(False)
    vars['1'] = Bit(True)
    for part in parts:
      part_name = part['chip_name']
      part_vars = part['vars']
      if part_name == 'Nand':
        a = vars[part_vars['a']].val
        b = vars[part_vars['b']].val
        if not vars[part_vars['out']]:
          vars[part_vars['out']] = Bit()
        vars[part_vars['out']].Nand(a=a, b=b)
      elif part_name == 'Not':
        a = vars[part_vars['in']].val
        if not vars[part_vars['out']]:
          vars[part_vars['out']] = Bit()
        vars[part_vars['out']].Not(a=a)
      elif part_name == 'And':
        a = vars[part_vars['a']].val
        b = vars[part_vars['b']].val
        if not vars[part_vars['out']]:
          vars[part_vars['out']] = Bit()
        vars[part_vars['out']].And(a=a, b=b)
      elif part_name == 'Or':
        a = vars[part_vars['a']].val
        b = vars[part_vars['b']].val
        if not vars[part_vars['out']]:
          vars[part_vars['out']] = Bit()
        vars[part_vars['out']].Or(a=a, b=b)
      else:
        next_parts = self.reader.read_parts(name=part_name)
        next_vars = {}
        for k, v in part_vars.items():
          if not vars[v]:
            vars[v] = Bit()
          next_vars[k] = vars[v]
        self.run(parts=next_parts, vars=next_vars)