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

def solve( array ):

    columns = list( zip( *array ) )
    rating = [ [0] * len( array[0] ) for _ in range( len(array) )]

    last = -1
    count = 0

    for y in range( len( array[0] ) ):

        for x in reversed( range( len( columns[y] ) ) ):

            if last == columns[y][x]:
                count += 1
            else:
                count = 0
                last = columns[y][x]

            rating[x][y] = copy.deepcopy( count )

        last = -1
        count = 0

    best_x = -1
    current_x = -1
    best_y = -1
    current_y = -1

    size = 0
    current_size = 0
    
    height = 0
    current_height = 0
    
    width = 0
    current_width = 0

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in rating]))
    print()
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in array]))

    for x in range( len(array) ):
        for y in range( len( array[0] ) ):
            
            print("[", x, y, "] Číslo:", array[x][y], "Rating:", rating[x][y])

            # Pro první položku v řádku
            if y == 0:
                print("Reset pro první")
                current_x = copy.deepcopy( x )
                current_y = copy.deepcopy( y )
                current_width = 1
                current_height = rating[x][y]
                current_size = current_width * current_height
            else:

                print("Else větev")
                current_width += 1

                # Stále pokračujeme, ale s menší hloubkou
                if rating[x][y] != current_height:
                    print("Zmenšuji hloubku")
                    # Je třeba zabránit změně hloubky pokud by to znamenalo zmenšení
                    # matice
                    if current_width * rating[x][y] >= current_size:
                        current_height = rating[x][y]
                        current_size = current_width * current_height
                    else:
                        current_size = current_width * current_height

                        
                else:
                    current_height = rating[x][y]
                    print("Aktualizuji velikost", current_size)
                    current_size = current_width * current_height
                    print(current_height)
                    print()

            # Pokud jsme našli lepší
            if current_size > size:
                print("better [", current_x, current_y, "], size", current_size)

                best_x = copy.deepcopy( current_x )
                best_y = copy.deepcopy( current_y )
                width = copy.deepcopy( current_width )
                height = copy.deepcopy( current_height )
                size = copy.deepcopy( current_size )
                continue
            
            """# V případě, že jde o jiné číslo
            if y > 0 and array[x][y] != array[x][y-1]:
                # Pokud jsme našli lepší
                if current_size > size:
                        
                    best_x = copy.deepcopy( current_x )
                    best_y = copy.deepcopy( current_y )
                    width = copy.deepcopy( current_width )
                    height = copy.deepcopy( current_height )
                    size = copy.deepcopy( current_size )

                current_x = copy.deepcopy( x )
                current_y = copy.deepcopy( y )
                current_width = 1
                current_height = rating[x][y]
                current_size = current_width * current_height

            
                continue
            """
    return best_x, best_y, width, height
    
matrix = loadFile( sys.argv[1] )
print( solve( matrix ) )
