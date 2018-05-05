def fibonacci(n):
    if n < 0:
        raise ValueError("n > 0")

    print(fibonacci.hints)
    print()

    if n < len( fibonacci.hints ):
        return fibonacci.hints[ n ]
    else:
        val = fibonacci(n-1) + fibonacci(n-2)
        if len(fibonacci.hints) == n:
            fibonacci.hints.append( val )
        return val

fibonacci.hints = [0, 1]

print("fibonacci( a )")
a = int(input("A = "))

print( fibonacci(a) )