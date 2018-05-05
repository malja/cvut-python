def binomial( k, n ):
    if n < k or n < 0 or k < 0:
        raise ValueError("n > k > 0")

    if k == 1 or k == (n-1):
        return n
    elif k == 0 or k == n:
        return 1

    return binomial( k, n - 1 ) + binomial( k-1, n-1)


print("( a nad b )")
a = int(input("A = "))
b = int(input("B = "))

print( binomial( b, a ) ) 
