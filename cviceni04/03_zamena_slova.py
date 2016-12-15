# Zadání:
#########
# Napište program, který čte standardní vstup a v načteném řetězci zamění 
# slovo Ahoj za slovo Cau.
# 
# Můžete využít vestavěné funkce find, replace, nebo Vaše funkce z předchozí
# úlohy.
#
# Pokud se ve vstupním řetězci objeví slovo Konec program skončí, ale i v tomto
# řádku nejdříve zamění Ahoj za Cau.
###############################################################################

def my_find(what, where):
    """
    Funkce pro nalezení podřetězce.
    Parametry:
    ----------
        what - Řetězec, který se hledá
        where - Prohledávaný řetězec
    Vrací:
    ------
        { start: index začátku, 
          end: index konce } - Pokud je řetězec nalezen
        False - Pokud není podřetězec nalezen
    """

    # Pokud je hledaný řetězec delší, než prohledávaný řetězec
    if len(what) > len(where):
        # nemá cenu hledat
        return False

    # Projde prohledávaný řetězec znak po znaku.
    for c in range(len(where)):
        # Pokud se hledaný řetězec v prohledávaném nachází na
        # pozici od aktuálního znaku dál
        if where[c:c+len(what)] == what:
            # Vrátí indexy začátku a konce
            return {
                "start": c,
                "end": c+len(what) }

    return False

def my_replace(what, where, new_value):
    """
    Funkce nahradí všechny výskyty hledaného řetězce za novou hodnotu
    Parametry:
    ----------
        what - Hledaný podřetězec
        where - Prohledávaný řetězec
        new_value - Nový řetězec, který bude nahrazen za výskyty
    """

    found = my_find(what, where)
    
    while found != False:
        
        start_string = where[:found["start"]]
        end_string = where[found["end"]:]
        where = start_string + new_value + end_string

        found = my_find( what, where )
    
    return where  

while True:
    line = input()
    line = my_replace("Ahoj", line, "Cau")
    index = my_find("Konec", line)
    print("> ", line)
    
    if (index != False):
        break
