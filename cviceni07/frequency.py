import sys
from collections import Counter

def loadFile( filename ):

    words = []

    with open(filename) as file:
        for line in file:

            # Kvůli poslednímu slovu
            line += " "
            word = ""

            for char in line:
                if not char.isalpha():
                    if len(word) > 0:
                        words.append( word.lower() )
                        word = ""
                    continue
                
                word += char

    return words

def countWordFrequencies( words ):
    words_sorted = sorted( words )
    unique_words = sorted( set( words_sorted ) )
    frequencies = []

    for unique in unique_words:
        frequencies.append(0)
 
        while True:
        
            if words_sorted[0] == unique:

                frequencies[-1] += 1
                words_sorted.pop(0)

                if len( words_sorted ) == 0:
                    break

            else:
                break

    return frequencies, unique_words

def printOutput( frequencies, words ):
    
    max_frequency = max( frequencies )
    
    for i in range( len( words ) ):
        print( "{:>14}:".format( words[i] ), "*" * int( ( 50* frequencies[i] ) / max_frequency ), sep="" )


array = loadFile( sys.argv[1] )

if ( len(array) == 0 ):
    exit()

freq, uniq = countWordFrequencies( array )
printOutput( freq, uniq )