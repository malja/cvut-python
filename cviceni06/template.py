import sys
import copy

def loadFile( name ):
    storage = []
    with open(name) as file:
        for line in file:

            l = []

            elements = line.replace("\n", "").split()
            for element in elements:
                if not element.isdigit():
                    print("ERROR")
                    exit()
                
                l.append( int(element) )
            
            storage.append( l )

    return storage

def getSubmatrix( matrix, x, y, size_x, size_y ):
    submatrix = []

    for x in range( x, x + size_x ):
        submatrix.append( matrix[x][y:y+size_y] )
    
    return submatrix

def matrixMinus( a, b ):
    value = 0
    for x in range( len(a) ):
        for y in range( len( a[0] ) ):
            value += abs( a[x][y] - b[x][y] )

    return value


def findBestMatch( a, b ):

    if len(a) >= len(b) and len(a[0]) >= len(b[0]):
    
        best_x = -1
        best_y = -1
        best_value = 0

        for x in range( 0, len(a)-len(b)+1 ):
            for y in range( 0, len(a[0])- len(b[0])+1 ):
                
                submatrix = getSubmatrix( a, x, y, len(b), len(b[0]))
                value = matrixMinus( submatrix, b )
         
                if best_x < 0 or best_y < 0:
                    best_x = x
                    best_y = y
                    best_value = copy.deepcopy( value ) 

                if value < best_value:
                    best_x = x
                    best_y = y
                    best_value = copy.deepcopy( value )

        return best_x, best_y

    else:
        return -1,-1


bigger = loadFile( sys.argv[1] ) 
smaller = loadFile( sys.argv[2] )
bestMatch = findBestMatch( bigger, smaller )
print( bestMatch[0], bestMatch[1] )