# Zadání:
#########
#
# Vytvořte program base.py, která ze standardního vstupu přečte řádku,
# která obsahuje desetinné číslo a druhou řádku, která obsahuje základ
# soustavy čísla z první řádky.
#
# Základ soustavy je v rozmezí 2 .. 36
#
# Pro soustavy o základu menším nebo rovno 10, obsahuje desetinné číslo
# pouze čísla od 0 .. základ soustavy - 1 a znak .
#
# Pro soustavy o základu větším než 10, obsahuje desetinné číslo čísla 
# 0,..,9 a písmena 'a', .. , 'z', ale hodnota 
# ord(znak)−odr(′a′) < zaklad_soustavy−10
#
# Desetinné binární číslo 
# 101.0101 = 1∗2^2 + 0∗2^1 + 1∗2^0 + 0∗2^(−1) + 1∗2^(−2) +0∗2^(−3) + 1∗2^(−4) = 5.3125
#
# Výstupem programu je zadané číslo převedené do desítkové soustavy 
# (tedy pro vstup 101.0101 bude výstup 5.3125).
# 
# Pokud je na vstupu špatně zadané číslo (obsahuje jiné znaky než povolené
# cifry a znak '.', případně obsahuje znak '.' vícekrát), pak vytiskne na
# výstup slovo “ERROR”
#
# Správnost vstupu základu soustavy nemusíte testovat.
###############################################################################

# Desetinné číslo
number = input()
# Základ číselné soustavy
base = int(input())

# Rozdělí načtený řetězec na část před a po desetinné čárce (tečce)
parts = number.split(".")

# Pokud vznikly více než dvě části - víc než 1 desetinná čárka, ohlásí chybu
if len(parts) != 2:
    print("ERROR")
    exit()

output = 0

# Pokusí se jak část před, tak i část po desetinné čárce převést na číslo 
# v zadané číselné soustavě
try:
    int(parts[0], base)
    int(parts[1], base)
except ValueError:
    print("ERROR")
    exit()

# Délka části celého čísla
len_integer = len(parts[0])+1
# Délka části za desetinnou čárkou
len_float = len(parts[1])+1

# Postupouje odzadu v rámci celého čísla
# a převede ho na adekvátní číslo v zadané soustavě
for i in range( 1, len_integer ):
    output += int(parts[0][-i], base) * base ** (i-1)

# To samé pro čísla za desetinnou čárkou
for i in range( 1, len_float ):
    output += int(parts[1][i-1], base) * base ** -i

print( output )
