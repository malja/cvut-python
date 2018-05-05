import sys
import keyword as kw
import tokenize

strings = [
    "'",
    '"'
]

operators = [
    "+", "-", "*", "**", "/", "//", "%", "<<", ">>", "&", "|", "^", "~", "<", ">", "<=", ">=", "==", "!="
]

separators = [
    "(", ")", "[", "]", "{", "}", ",", ":", ".", ";",
    "@", "=", "->", "+=", "-=", "*=", "/=", "//=", "%=",
    "@=", "&=", "|=", "^=", ">>=", "<<=", "**="
]

# Získá všechny klíčová slova aktuální verze pythonu
keywords = kw.kwlist

def isNumber( string ):
    try:
        int( string, 0 )
        return True

    except ValueError:
        return False

def tokenizeFile( file_name ):

    tokens = ""

    with open( file_name ) as file:
        tokens = list( tokenize.generate_tokens( file.readline ) )
    
    output = []
    current_string = ""
    already_in_string = False

    for token in tokens:

        # Proměnná nebo keyword
        if token[0] == tokenize.NAME:

            # Pokud se string nachází v poli klíčových slov
            if token[1] in keywords:
                output.append( "Key: " + token[1] )
            # Jinak je to jméno proměnné
            else:
                output.append( "Var: " + token[1] )     

        # Operátor nebo separátor
        elif token[0] == tokenize.OP:

            # Pokud se string nachází v poli separátorů
            if token[1] in separators:
                output.append( "Sep: " + token[1] )
            else:
                output.append( "Ope: " + token[1] )

        # Číslo 
        elif token[0] == tokenize.NUMBER:

            if isNumber( token[1] ):
                output.append( "Int: " + token[1] )
            else:
                output.append( "Rea: " + token[1] )

        # Řetězec
        elif token[0] == tokenize.STRING:
            
            innerText = token[1]

            while len(innerText) > 0 and (innerText[0] == "'" or innerText[0] == '"'):
                innerText = innerText[1:]

            while len(innerText) > 0 and (innerText[-1] == "'" or innerText[-1] == '"'):
                innerText = innerText[:-1]

            innerText = innerText.replace("\\", "")

            output.append( "Str: " + innerText )

    return output

tokens = tokenizeFile( sys.argv[1] )

for token in tokens:
    print( token )