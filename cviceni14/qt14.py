import sys

def load_dict(filename):

    with open(filename) as file:
        for line in file:
            return line.replace("\n", "").split(" ")

def load_file( filename ):

    content = []

    with open(filename) as file:
        for line in file:
            content.append( line.replace("\n", "").split(" ") )

    return content

def caesar( text, shift ):
    cypher = ""

    # Proje text znak po znaku

    for char in text:
        # ASCII kód aktuálního znaku
        code = ord(char)

        # Pro velká písmena musí být ASCII kód v daném rozmezí
        if ( code >= 65 and code <= 90 ):

            # Písmeno se zašifruje tak, že se nejprve od jeho 
            # ASCII kódu odečte kód písmene A. K tomu se přičte posun.
            # Pomocí modula se výsledek udrží v rozmezí.
            # Nakonec se opět přičte kód Ačka.
            cypher += chr( (code - ord("A") + shift)%26 + ord("A") )
        
        # Pro malá písmena
        elif ( code >= 97 and code <= 122):
            
            cypher += chr( (code - ord("a") + shift)%26 + ord("a") )
        
        # Pro ostatní znaky
        else:

            cypher += char
    
    return cypher

def most_common(lst):
    return max(set(lst), key=lst.count)

dictionary = load_dict( sys.argv[1] )
content = load_file( sys.argv[2] )

for line in content:

    codes = []

    for cypher in range(0, 25+1):
        for c in line:
            for d in dictionary:

                #print (c, d, caesar(c, cypher))

                if caesar(c, cypher) == d:
                    codes.append(True)
                    break
                else:
                    continue

        if len(codes) >= len(line):
            print(cypher)
        
        codes = []
            

        