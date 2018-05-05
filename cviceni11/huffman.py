# Zadání:
#########
#
# Úkolem je implementovat kompresi textu Huffmanovým kódováním.
#
# Vstup: 
#   * dva argumenty na příkazové řádce: jméno vstupního souboru a jméno
#     výstupního souboru
#
# Vstupní soubor je textový soubor, který obsahuje různě dlouhé řádky textu,
# text obsahuje pouze písmena abecedy (malá a velká), a číslice.
#
# Předpokládejte rozumně dlouhé řádky (např. max. 1000 znaků na řádku).
#
# Program načte vstupní soubor, spočítá četnost jednotlivých znaků a vypočte
# algoritmem Huffmanova kódování jejich komprimovaný obraz.
#
# Do výstupního souboru bude uloženo toto kódování ve formě: znak kod
# 
# Na každém řádku bude uveden jedno písmeno a jeden kód.
# Počet výstupních řádků je tedy roven délce abecedy (počet znaků), které jsou 
# obsaženy ve vstupním souboru.
# Kód vytvořte pouze pro velká a malá písmena a pro číslice, ignorujte
# white-space znaky.
#
# Na pořadí písmen ve výstupním souboru nezáleží.
# Na velikosti písmen záleží (např. znaky 'a' a 'A' budou mít rozdílný kód).
# Odevzdejte do odevzdávacího systému jako huffman.py, úkol HW10.
# 
# Příklad:
"""
       aaaaaa bbbb cc dddd ee
       d
       aa d d
       d a b c
"""
# Příklad spuštění:
#
#       > python3 huffman.py input.txt output.txt 
#
# Výstup v output.txt bude obsahovat:
"""
       c 100
       e 101
       a 00
       d 01
       b 11
"""
###############################################################################

import sys # Nutný pro zjištění parametrů příkazové řádky
import copy # Jen pro můj duševní klid

# Následující import se moc hodí při ladění, po odkomentování je možné pomocí
#
#   pp = pprint.PrettyPrinter( indent = 4)
#   pp.pprint( <sem_vloz> )
#
# nechat pěkně vypsat dictionary a pole.  
# import pprint


def countCharactersInFile( filename ):
    """
    Spočítá počet výskytů znaků anglické abecedy a čísel. Rozlišuje mezi 
    velkými a malými písmeny.

    Parametry:
    ----------
        filename: string
            Jméno souboru, ve kterém má znaky spočítat.

    Vrací:
    ------
        list
            Pole složené z dictionary:
            { 
                "name": Znak číslice či písmena
                "count": Počet výskytů v souboru
            }
            Jednotlivé slovníky jsou seřazeny vzestupně podle hodnoty count.
    """
    characters = []

    # Otevře soubor ke čtení
    with open( filename ) as file:

        # Projde každou řádku
        for line in file:

            # Projde každý znak v řádku
            for char in line:
                
                # Pokud jde o znak nebo číslo
                if char.isalpha() or char.isdecimal():

                    # Pokusí se znak vyhledat v poli characters. Pokud neexistuje, vrátí
                    # None.
                    char_data = next( (n for n in characters if n["name"] == char), None )
                    
                    # Pokud jde o první výskyt tohoto znaku
                    if char_data == None:
                        # Vytvoří jeho reprezentaci a vloží jí na seznam
                        char_data = {"name": char, "count": 0 }
                        characters.append( char_data )

                    # Zvýší počítadlo o 1
                    char_data["count"] += 1

    # Vrátí pole slovníků seřazené vzestupně podle četnosti výskytu znaků v souboru
    return sorted( characters, key = lambda elem: elem["count"] )

def buildHuffmanTree( probability ):
    """
    Vystaví strom pro další zpracování huffmanovým kódováním.
    
    Parametry:
    ----------
        probability: list
            Pole slovníků ve formátu:
            { 
                "name": Znak číslice či písmena
                "count": Počet výskytů v souboru
            }
            Pole musí být seřazeno od nejmenšího po nejvyšší výskyt.

    Vrací:
    ------
        dictionary
            Slovník ve formátu:
            {
                "name": Znak/číslo (pokud jde o počítaný znak) nebo prázdný 
                        řetězec (pokud jde o zástupný node)
                "count": Hodnota node
                "left:  Uvedeno jen pokud je "name" prázdné. Obsahuje
                        slovník.
                "right": Uvedeno jen pokud je "name" prázdné. Obsahuje
                         slovník.
            }
    """

    # Nechci upravovat originální parametr
    # Jen pro sichr, možná je to tu navíc :(
    tree = copy.deepcopy( probability )

    # Dokud nezbývá jen jeden parametr
    while len( tree ) > 1:

        # Vezme dva vrcholy s nejmenší hodností (nejmenší count)
        # Pole je seřazeno od nejmenších po největší, proto stačí pop
        right = tree.pop(0) # Vpravo jsou menší čísla, aby to vycházelo
        left = tree.pop(0)

        # Vytvoří se rodičovský node
        parent = {
            "name": "", # Prázdné jméno značí "rodičovský" node
            "count": left["count"] + right["count"],
            "left": left,
            "right": right,
        } 

        # Přidá rodičovský node zpět
        tree.append( parent )

        # Opětovně seřadí pole
        tree = sorted( tree, key = lambda elem: elem["count"] )
    
    # Vrací jen poslední slovník, pole je nadbytečné
    return tree[0]
    
def getHuffmanCoding( tree, prefix="", code = {} ):
    """
    Projde rekurzivně předaný strom a ohodnotí jednotlivé znaky dle
    pravidel Huffmanova kódování.
    To znamená, že hrana jdoucí od svého rodiče nalevo, má
    ohodnocení 0 a hrana napravo ohodnocení 1.

    Ohodnocení samotného vrcholu je tvořen posloupností kódů

    Parametry:
    ----------
        tree: dictionary
            Slovník reprezentující strom, který se má projít
        
        prefix: string
            Řetězec obsahující kód cesty k tomuto node
        
        code: dictionary
            Slovník obsahujcí páry písmen/číslic (klíč) a jejich kódu.

    Vrací:
    ------
        dictionary
            Slovník obsahující páry písmen/čísli (klíč) a jejich kódu.
    """

    # Pokud je potomek nalevo jen "rodičovský node"
    if tree["left"]["name"] == "":
        getHuffmanCoding( tree["left"], prefix+"0", code)
    else:
        # Node je znak/číslo, rovnou vytvoří jeho kód
        code[ tree["left"]["name"] ] = prefix+"0"

    # Pokud je potomek napravo jen "rodičovský node"
    if tree["right"]["name"] == "":
        getHuffmanCoding( tree["right"], prefix+"1", code )
    else:
        # Node je znak/čéslo, rovnou vytvoří kód
        code[ tree["right"]["name"] ] = prefix+"1"

    return (code)


# Počet parametrů příkazové řádky
argc = len( sys.argv )

# Potřebujeme tři parametry
if argc != 3:
    print("Použijte:")
    print("huffman.py input_file_name output_file_name")
    exit()

# Frekvence jednotlivých znaků
frequency = countCharactersInFile( sys.argv[1] )

# Stromová reprezentace
tree = buildHuffmanTree( frequency )

# Huffmanovo kódování
codes = getHuffmanCoding( tree )

# Zápís do souboru
with open( sys.argv[2], "w") as f:
    for key in codes:
        print( key, codes[key], file=f )              
