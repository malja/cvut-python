k=input()

try:
    k=int(k)
except ValueError:
    print("ERROR")
    exit()

if k<1 or k>99:
    print("ERROR")
    exit()

def gcd2(a, b):
    i=0
    while b != 0:
        i+=1
        a, b = b, a % b
    return a

for radek in range(1, k+1):
    for sloupec in range (1, k+1):
        if gcd2(radek, sloupec) == 1:
            print(".", end="")
        else:
            print("x", end="")
    print()

