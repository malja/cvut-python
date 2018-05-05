message = "T E * A * Q Y S * * * S E U * * * * N I * O * *".split()

stack = []
output = ""

for i in message:

    if ( i.isalpha() ):
        stack.append( i )
    elif ( i == "*" ):
        output += stack.pop() 
    
print( output )