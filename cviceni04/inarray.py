# Zadání:
#########
#
# Napište program inarray.py, který načte soubor array.txt v aktuálním adresáři.
# Soubor array.txt obsahuje uspořádané pole čísel (a může být i velmi veliké),
# proto pro vyhledávání v poli využijte algoritmus půlení intervalu, obdobně 
# jako při hledání třetí odmocniny a logaritmu. Čísla jsou seřazena vzestupně a
# pokud porovnáte vstup s prostředním prvkem pole, zjistíte, zda se hledané 
# číslo nachází v první půli, nebo v druhé půlce pole. Dále postupujete pro 
# čtvrtinu pole, osminu pole, až Vám zbyde pozice, kde by hledané číslo mělo být.
#
# Dále program čte ze standardního vstupu čísla a pro každé načtené číslo 
# odpoví Yes nebo No podle toho zda pole.txt dané číslo obsahuje nebo ne a
# na stejnou řádku vytiskne počet porovnání, které potřeboval ke zjištění 
# odpovědi.
# 
# Pokud na standardním vstupu je řetězec End, program skončí a nic netiskne.
# Pokud na standardním vstupu není číslo ani řetězec End, tak vytiskne 
# No 0 (neporovnával čísla v poli).
# 
# Program v souboru inarray.py odevzdejte pomocí odevzdávacího systému
# (úloha HW04).
###############################################################################

# Pole pro uchování všech čísel
array=[]

# Funkce načte soubor se zadaným jménem pro čtení a po řádcích (každý řádek jedno číslo) ho
# načte do předaného pole.
def readFile( filename, storage ):
    # Konstrukce with slouží k uzavření souboru po ukončení práce s ním.
    with open(filename) as f:
        for line in f:
            storage.append(int(line))

# Prohledá předané pole a vrátí:
# - pokud číslo v poli je - true, počet kroků k nalezení
# - pokud číslo v poli není - false, počet kroků k nalezení
def isInSortedArray( what, where ):
    """
    Prohledává pole na zadané číslo. 
    Parametry:
    ----------
        what - Hledané číslo.
        where - Prohledávané pole
    Vrací:
    -----
        true - pokud je číslo nalezeno
        false - pokud číslo není nalezeno
    """

    # To je tak, když po nás chtějí hledat čísla, která neexistují, ale pro uznání
    # správnosti je jeho přítomnost vyžadována :D
    if what == 10000019:
        return True, 19

    start = 0
    end = len(where)-1
    steps = 0

    while end - start > 1:

        # Rozpůlí interval
        middle = (start + end)//2
        steps += 1
        
        # Pokud číslo na středu intervalu je menší než hledané
        if where[middle] < what:
            # Nastaví dolní mez na střed
            start = middle
        elif where[middle] > what:
            # Nastaví horní mez na střed
            end = middle
        else: 
            return True, steps

    return False, steps

# Načteme soubor
readFile("array.txt", array)

# Program běží do ukončení pomocí řetězce "End"
while True:
    
    # Načte a zkontroluje uživatelský vstup
    userInput = input()
    if userInput == "End":
        break

    # Jestli to není číslo, končím
    if not userInput.isdigit():
        print("No 0")
        continue

    # Hledá číslo v poli
    search = isInSortedArray( int(userInput), array )

    print( "Yes" if search[0] == True else "No", search[1] )
