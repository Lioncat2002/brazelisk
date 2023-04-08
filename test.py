from brazelisk import brazelisk

def test():
    x = brazelisk.Symbol("x")
    y = brazelisk.Symbol("y")

    expr1 = x**y + y * x * y + y**y
    expr2 = x**y - y * x * y + y**y

    print(expr1-expr2)


test()
