class Bit:
    def __init__(self, val: bool = False) -> None:
        self.val = val

    def nand_(self, a: bool, b: bool) -> None:
        self.val = not (a and b)

    def not_(self, a: bool) -> None:
        self.val = not a

    def and_(self, a: bool, b: bool) -> None:
        self.val = a and b

    def or_(self, a: bool, b: bool) -> None:
        self.val = a or b

    def __str__(self) -> str:
        return f"Bit({self.val})"

    __repr__ = __str__
