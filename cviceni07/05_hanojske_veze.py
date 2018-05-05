def hanojske_veze(n, a, b, c):
    if n > 0:

        hanojske_veze( n-1, a, c, b )
        b.append( a.pop() )
        print("A=", A, "B=", B, "C=", C)
        hanojske_veze( n-1, c, b, a )
        hanojske_veze.counter += 1

hanojske_veze.counter = 0


A = []
B = []
C = []

kruhu = int(input("Počet kruhů:"))
while kruhu > 0:
    A.append(kruhu)
    kruhu -= 1

hanojske_veze(len(A), A, B, C)
print(hanojske_veze.counter)       