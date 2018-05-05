start = list(map(int, input().split()))

def inArray(x, y, array):
    return x > 0 and x < len( array[0] ) and y > 0 and y < len( array )

def fill( x, y ):
    m=[
        [0,0,1,0,0,1,0,0,0,0],
        [0,0,1,0,0,1,0,0,0,0],
        [0,0,1,1,0,1,0,0,0,1],
        [0,0,1,0,0,0,1,0,1,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,1,1,0,1,0,0,0,0],
        [0,0,1,0,1,1,1,1,0,0],
        [0,0,1,0,0,1,0,1,1,1],
        [0,0,1,0,0,1,0,0,0,0],
        [0,0,1,0,0,1,0,0,0,0] ]

    if not inArray(x, y, m):
        return m

    stack = []

    if m[ x ][ y ] == 0:
        m[x][y] = 2
        stack.append( [ x, y ] )
    else:
        return m
    
    while ( len( stack ) != 0 ):
        a = stack[0][0]
        b = stack[0][1]

        m[a][b] = 2

        if inArray( a - 1, b, m ):
            if m[ a -1 ][b] == 0:
                stack.append([a-1, b])
        
        if inArray( a + 1, b, m):
            if m[ a + 1 ][b] == 0:
                stack.append([a+1,b])

        if inArray( a, b - 1, m):
            if m[ a ][b -1] == 0:
                stack.append([a, b-1])

        if inArray( a, b+1, m):
            if m[ a ][b+1] == 0:
                stack.append([a, b+1])

        stack.pop(0)

    return m

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in fill( start[0], start[1] ) ]))
        



    

    