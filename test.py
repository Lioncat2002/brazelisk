from brazelisk import brazelisk

def test():
    x = brazelisk.Symbol("x")
    y = brazelisk.Symbol("y")

    expr1 = x+x+y/y
    
    print(expr1)


test()
