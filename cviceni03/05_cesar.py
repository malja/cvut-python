# Zadání:
#########
#
# Napište program, který přečte jednu řádku ze vstupu s textem složeným pouze
# z písmen a mezery a druhou řádku s číslem definujícím posunutí písmen v 
# Césarově šifře.
#
# Program na výstup vypíše řetězec zašifrovaný posunutím písmen o zadanou 
# hodnotu.
#
# Ascii hodnota znaku se získá funkcí ord('A'), opačně znak z celého čísla 
# získáte pomocí funkce chr(65)
#
# Je nutné posouvat velká písmena na velká písmena, malá písmena na malá 
# písmena a mezeru ponechat jako mezeru
###############################################################################

# A = 65, Z = 90
# a = 97, z = 122
# Znaku - 26

string = input("Zadej text k šifrování:")
shift = int(input("Zadej posun:"))%26

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

print( caesar(string, shift) )
