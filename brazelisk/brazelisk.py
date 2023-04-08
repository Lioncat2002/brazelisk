class Symbol:
    def __init__(self, expr):
        self.expr = expr

    def __add__(self, other):
        return Symbol(f"({self.expr})+({other.expr})")

    def __sub__(self, other):
        return Symbol(f"({self.expr})-({other.expr})")

    def __mul__(self, other):
        return Symbol(f"({self.expr})*({other.expr})")

    def __truediv__(self, other):
        return Symbol(f"({self.expr})/({other.expr})")

    def __pow__(self, other):
        return Symbol(f"({self.expr})**({other.expr})")

    def __repr__(self):
        return self.expr
