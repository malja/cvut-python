# Zadání:
#########
# 
# Vytvořte program, který ze standardního vstupu přečte řádku, obsahující
# buď číslo v desítkové soustavě nebo číslo zapsané slovy bez háčků např.
# dvestepadesatsedmtisictristasedmdesatpet a toto číslo převede do opačného
# zápisu. Pokud vstup neodpovídá ani jedné z těchto možností, vytiskne 
# 'ERROR' a skončí.
#
# Vstup:
# > dvestepadesatsedmtisictristasedmdesatpet
# Výstup:
# > 257375
#
# Vstup:
# > 543210 
# Výstup:
# petsetctyricettritisicedvestedeset
#
# Všechny čísla jsou pouze celá čísla v rozsahu 1 až 999999.
# 
# Pro slovni cislo jsou použity tyto slovni vyjadreni: jeden, dva, tri, 
# ctyri, pet, sest, sedm, osm, devet, deset, jedenact, dvanact, trinact, 
# ctrnact, patnact, sestnact, sedmnact, osmnact, devatenact, dvacet, tricet,
# ctyricet, padesat, sedesat, sedmdesat, osmdesat, devadesat, sto, dveste, 
# trista, ctyrista, petset, sestset, sedmset, osmset, devetset, tisic, tisice.
#
# Pozn.: V češtině je správně “dvatisice”, ale lze napsat “stodvatisic” a
# “stodvatisice”. Po Vás požadujeme řešení ve tvaru “stodvatisice”.
###############################################################################

# Vstupem je číslo v desítkové soustavě, nebo řetězec bez mezer
userInput = input()

# Funkce pro kontrolu, zda jde o číslo
# Je mnoho lepších přístupů, ale o nich nám řekli až časem ;)
def isDigit( what ):
    try:
        int(what)
    except ValueError:
        return False

    return True

def find(what, where):
    """
    Najde první výskyt prvku pole v řetězci.
    Parametry:
    ----------
        what - Pole s prvky, které se mají hledat
        where - Prohledávaný řetězec
    Vrací:
    ------
        [ 
            "start": Začátek výskytu, 
            "end": konec výskytu,
            "element_id": ID nalezeného prvku ]
        nebo
        False - Pokud není žádný prvek pole v řetězci nalezen
        
    """

    # Projde pole what pozpátku
    for i, element in enumerate(reversed(what) ):
    
        # Pokud je prvek pole delší než celý řetězec, nemá cenu ho hledat
        if len(element) > len(where):
            continue

        # Projde řetězec znak po znaku
        for c in range(len(where)):

            # Pokud se hledaný element vyskytuje v řetězci od aktuálního
            # znaku dál
            if where[c:c+len(element)] == element:
                return {    "start": c, 
                            "end": c+len(element),
                            "element_id": i }

    return False

def findAndRemove(what, where):
    """
    Najde výskyt všech prvků pole v řetězci a odstraní je-
    Parametry:
    ----------
        what - Pole hledaných prvků k odstranění
        where - Prohledávaný řetězec
    """
    for element in what :
        if (len(where) == 0):
            break
        where= where.replace(element, "")

    return where

numbers = [
        "jeden", "dva", "tri", "ctyri", "pet", "sest", "sedm", "osm", "devet", "deset", "jedenact", "dvanact", "trinact", "ctrnact", "patnact", "sestnact", "sedmnact", "osmnact", "devatenact"
]

tens = [
        "dvacet", "tricet", "ctyricet", "padesat", "sedesat", "sedmdesat", "osmdesat", "devadesat"
]

hundreds = [
        "sto", "dveste", "trista", "ctyrista", "petset", "sestset", "sedmset", "osmset", "devetset"
]

thousands = [
        "tisic", "tisic", "tisice", "tisice", "tisice", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic", "tisic"
]


def stringToNumber( what ):
    """
    Převede řetězec na číslo.
    Parametry:
    ----------
        what - Řetězec pro převedení na číslo.
    """    
    number = 0

    # Najde v poli stovek odpovídající řetězec
    coords = find(hundreds, what)
    # Pokud se něco našlo
    if not coords == False:
        # Zmenší číslo o první znak
        what = what[ coords["end"]: ]

        # Vypočítá číselnou hodnotu řetězce v závislosti na indexu v poli 
        # hundreds.
        number = (len(hundreds) - int(coords["element_id"]) ) * 100
    
    # Najde v poli desítek odpovídající řetězec
    coords = find(tens, what)
    # Pokud se něco našlo
    if not coords == False:
        # Zmenší číslo o první znak
        what = what[ coords["end"]: ]
        # Vypočítá číselnou hodnotu řetězce v závislosti na indexu v
        # poli tens.
        number += (len(tens) - int(coords["element_id"]) + 1) * 10

    # Najde v poli jednotek odpovídající řetězec
    coords = find(numbers, what)
    if not coords == False:

        # Vypočítá číselnou hodnotu řetězce v závislosti na indexu v
        # poli numbers
        number += len(numbers) - int(coords["element_id"])

    return number

    

def upToThousandToString( what, addThousand=False ):
    """
    Převede zadané číslo na jeho textovou reprezentaci.
    Parametry:
    ----------
        what - Číslo k převedení na řetězec
        addThousand - Pokud je číslo reprezentace tisíců, vložte true
    """
    temp = ""

    what = str(int(what))

    # Pokud je číslo větší než 100, tzn má stovky
    if int(what) >= 100:
        # Získá první číslo a převede ho na reprezentaci uloženou v poli stovek
        temp += hundreds[ int(what[0])-1 ]
        
        # Odstraní první číslo
        what = what[1:]

    # Pokud je číslo nulové, už jsme něco zpracovali a máme přidat tisíce
    if int(what) == 0 and temp != "" and addThousand:
        # Vloží řetězec "tisíc"
        temp += thousands[0]
        return temp

    #  Pokud je číslo mmez 0 a 20
    if int(what) < 20 and int(what) > 0:
        
        # Přidá na výstup řetězec reprezentující číslo 
        temp += numbers[ int(what) -1]

        # Pokud se mají přidat tisíce
        if addThousand:
            temp += thousands[ int(what) ]

    # Pokud je číslo větší než 20
    elif int(what) >= 20:
        
        # Pokud je první číslo nenelové
        if( int(what[0]) != 0):

            temp += tens[ int(what[0]) -2 ]
        
        # Pokud je druhé číslo nenulové
        if(int(what[1]) != 0):
            temp += numbers[ int(what[1])-1 ]
        
        # Pokud se mají přidat tisíce
        if addThousand:
            temp += thousands[ int(what[1]) ]

    return temp

# Pokud je zadáno číslo, je třeba ho převést na odpovídající slovní reprezentaci:
# 73 - sedmdesattri
if isDigit( userInput ):

    output = ""

    # Kontrola, zda je číslo v rozsahu
    if int(userInput) > 999999 or int(userInput) < 1:
        print("ERROR")
        exit()

    # Pokud má vstup méně než nebo právě tři znaky, nemá tisíce
    if len(userInput) <= 3:
        # Získá číslo jako textovou reprezentaci
        output += upToThousandToString( userInput )
    
    # Pokud má číslo více než tři znaky, má tisíce.
    else:

        # Vloží text odpovídající části tisíců na výstup
        output += upToThousandToString( userInput[ :len(userInput)-3 ], True )

        # Vloží text odpovídající části stovek na výstup
        output += upToThousandToString( userInput[len(userInput)-3:] )

    print(output)
    exit()

# Jde o řetězec. Budu tak dlouho odstraňovat povolené řetězce
# (tzn. ty, které mám v některém z polí nahoře) dokud:
#   - nezbyde prázdný řetězec (úspěch)
#   - nejde nahradit žádný podřetězec za číslo (neúspěch)
# Pokud řetězec projde tímto primitivním testem, zpracuji zvlášť část
# tisíců (pokud existuje) a část stovek a výsledek vypíšu 
else:

    # Uložení do dočasné proměnné
    test = userInput

    # Smaže všechny mě známé řetězce
    test = findAndRemove( ["tisice", "tisic"], test)
    test = findAndRemove( hundreds, test)
    test = findAndRemove( tens, test)
    test = findAndRemove( reversed(numbers), test)

    # Pokud zbyl ještě nějaký řetězec, který neznám, jde o špatně zadaný vstup
    if test != "":
        print("ERROR")
        exit()

    
    coords = find( ("tisic", "tisice") , userInput)
    # Text obsahuje reprezentaci pouze stovek
    if coords == False:
        # Převede část stovek na odpovídající číslo
        print(stringToNumber(userInput))
        exit()
    # Jestliže se v textu vyskytuje text tisíc/e, rozdělím ho na dvě části
    else:
        # Část tisíců a část stovek
        print(stringToNumber(userInput[:coords["start"]]) * 1000 + stringToNumber(userInput[coords["end"]:]))
        exit()
        
    
 



