# Zadání:
#########
# Napište funkci my_find(a,b), která v řetezci a hledá řetězec b (nepoužívejte
# vestavěnou funkci find). Pokud řetězec najde, vrátí index jeho prvního 
# výskytu zleva. Pokud řetězec nenajde, vrátí -1.
#
# Napište funkci my_replace(a,b,c), která v řetězci a nahradí všechny výskyty
# řetězce b řetězcem c.
#
# Ve funkcích používejte pouze funkce len(s) - délka řetězce, s[i] znak na 
# pozici i, s[i:j] podřetezec od i do j, resp s[:j], s[i:], podřetězec od 
# počátku do j, resp. od i do konce.
#
###############################################################################

v_cem = input("Slovo:")
co = input("CO:")

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

print( my_find(co, v_cem))
print( my_replace(co, v_cem, "baf"))
