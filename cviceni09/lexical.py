# Zadání:
#########
#
# Proveďte lexikální analýzu Pythonovského programu, který může obsahovat pouze následující lexikální termy:
#
# - Str: Řetězec - začíná znaky
#    
#     ',",''',"""
#
# a může obsahovat sekvenci se znakem \. Pokud obsahuje řetězec sekvenci se znakem \X (X reprezentuje nějaký znak
# z množiny \,',”,+,-), pak se do řetězce vloží pouze znak X.
#
# - Int: Celé číslo - integer:
#
#       integer        ::=  decimalinteger | octinteger | hexinteger | bininteger
#       decimalinteger ::=  nonzerodigit digit* | "0"+
#       nonzerodigit   ::=  "1"..."9"
#       digit          ::=  "0"..."9"
#       octinteger     ::=  "0" ("o" | "O") octdigit+
#       hexinteger     ::=  "0" ("x" | "X") hexdigit+
#       bininteger     ::=  "0" ("b" | "B") bindigit+
#       octdigit       ::=  "0"..."7"
#       hexdigit       ::=  digit | "a"..."f" | "A"..."F"
#       bindigit       ::=  "0" | "1"
#
# - Rea: Reálné číslo - viz úloha 2
# - Key: Klíčová slova Pythonu
# - Var: Proměnné - začíná písmenem a pak může obsahovat písmena, čísla a znak _
# - Ope: Operátory:
#
#       +       -       *       **      /       //      % 
#       <<      >>      &       |       ^       ~
#       <       >       <=      >=      ==      !=
#
# - Sep: Oddělovače:
#
#       (       )       [       ]       {       }
#       ,       :       .       ;       @       =       ->
#       +=      -=      *=      /=      //=     %=      @=
#       &=      |=      ^=      >>=     <<=     **=
#
# Předpokládejte, že je program syntakticky správně. Komentáře neuvažujte, předpokládejte, že program je bez komentářů.
# Progam lexical.py načte soubor zadaný jako vstupní parametr a vytiskne na výstup jednotlivé lexikální termy.
#
# Příklad
# -------
#
# Vstup:
"""
def funkce(a,b):
    c=''
    a**=b
    if a<b:
        print('ahoj\'ky',a)
    else:
        print(0xff,0b11101,0o777,.90e-10,123E+5,c)
        print('''To je dlouhy
        retezec pres mnoho
        radku''')
funkce(-256+356,.85**.33)
"""
#
# pak je výstupem Vašeho programu:
#
"""
Key: def
Var: funkce
Sep: (
Var: a
Sep: ,
Var: b
Sep: )
Sep: :
Var: c
Sep: =
Str: 
Var: a
Sep: **=
Var: b
Key: if
Var: a
Ope: <
Var: b
Sep: :
Var: print
Sep: (
Str: ahoj'ky
Sep: ,
Var: a
Sep: )
Key: else
Sep: :
Var: print
Sep: (
Int: 0xff
Sep: ,
Int: 0b11101
Sep: ,
Int: 0o777
Sep: ,
Rea: .90e-10
Sep: ,
Rea: 123E+5
Sep: ,
Var: c
Sep: )
Var: print
Sep: (
Str: To je dlouhy
        retezec pres mnoho
        radku
Sep: )
Var: funkce
Sep: (
Ope: -
Int: 256
Ope: +
Int: 356
Sep: ,
Rea: .85
Ope: **
Rea: .33
Sep: )
"""
#######################################################################################################################

import sys
import keyword as kw
import tokenize

separators = [
    "(", ")", "[", "]", "{", "}", ",", ":", ".", ";",
    "@", "=", "->", "+=", "-=", "*=", "/=", "//=", "%=",
    "@=", "&=", "|=", "^=", ">>=", "<<=", "**="
]

# Získá všechny klíčová slova aktuální verze pythonu
keywords = kw.kwlist

def isNumber(string):
    try:
        int(string, 0)
        return True

    except ValueError:
        return False

def tokenizeFile(file_name):

    tokens = ""

    with open(file_name) as file:
        tokens = list(tokenize.generate_tokens(file.readline))
    
    output = []
    current_string = ""
    already_in_string = False

    for token in tokens:

        # Proměnná nebo keyword
        if token[0] == tokenize.NAME:

            # Pokud se string nachází v poli klíčových slov
            if token[1] in keywords:
                output.append("Key: " + token[1])
            # Jinak je to jméno proměnné
            else:
                output.append("Var: " + token[1])

        # Operátor nebo separátor
        elif token[0] == tokenize.OP:

            # Pokud se string nachází v poli separátorů
            if token[1] in separators:
                output.append("Sep: " + token[1])
            else:
                output.append("Ope: " + token[1])

        # Číslo 
        elif token[0] == tokenize.NUMBER:

            if isNumber( token[1] ):
                output.append("Int: " + token[1])
            else:
                output.append("Rea: " + token[1])

        # Řetězec
        elif token[0] == tokenize.STRING:
            
            innerText = token[1]

            # innerText obsahuje uvozovky z řetězce. Je třeba je odstranit
            if (innerText.startswith('"""') and innerText.endswith('"""')) or \
               (innerText.startswith("'''") and innerText.endswith("'''")):
                # Odstranění tří uvozovek
                innerText = innerText[3:-3]
            else:
                # Odstranění standardních uvozovek
                innerText = innerText[1:-1]

            innerText = innerText.replace("\\", "")

            output.append("Str: " + innerText)

    return output

tokens = tokenizeFile(sys.argv[1])

for token in tokens:
    print(token)