class Symbol:
    def __init__(self, expr):
        self.expr = expr

    def __add__(self, other):

        if isinstance(other,Symbol):
            if self.expr==other.expr:
                return Symbol(f"2*{self.expr}")
            return Symbol(f"{self.expr}+{other.expr}")
        return Symbol(f"{self.expr}+{other}")

    def __sub__(self, other):
        if isinstance(other,Symbol):
            if self.expr==other.expr:
                return Symbol(f"")
            return Symbol(f"{self.expr}-{other.expr}")
        return Symbol(f"{self.expr}-{other}")

    def __mul__(self, other):
        if isinstance(other,Symbol):
            if self.expr==other.expr:
                return Symbol(f"{self.expr}**2")
            return Symbol(f"{self.expr}*{other.expr}")
        return Symbol(f"{self.expr}*{other}")

    def __truediv__(self, other):
        if isinstance(other,Symbol):
            if self.expr==other.expr:
                return Symbol(f"1")
            return Symbol(f"{self.expr}/{other.expr}")
        return Symbol(f"{self.expr}/{other}")

    def __pow__(self, other):
        return Symbol(f"{self.expr}**{other}")

    def __repr__(self):
        return self.expr
