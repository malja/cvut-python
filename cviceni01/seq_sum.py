# Zadání:
#########
#
# Vytvořte program který ze standardního vstupu přečte jednu řádku, 
# která obsahuje posloupnost celých čísel x1,…,xn a v této posloupnosti
# najde nejdelší neklesající posloupnost xi ≤ xi+1 ≤ … ≤ xi+j a na 
# výstup vytiskne její délku a na další řádek její součet.
#
# Pokud je v posloupnosti čísel více stejně dlouhých neklesajících 
# posloupností, pak program hledá tu s největším součtem.
#
# Pro načtení vstupu můžete použít příkaz:
# > nums = list(map(int, input().split()))
###############################################################################

# V numbers bude uloženo pole s jednotlivými čísly 
# [5 12 15 24 6 13 16 25 28]
numbers = list(map(int, input().split()));

# Počítadlo sumy
currSum = 0;
prevSum = 0;

# ... délky
currLen = 0;
prevLen = 0;

# Projde všechna čí­sla od 1 do počtu prvků v poli numbers
for i in range(1, len(numbers) ):

    # Pokud je aktuální prvek větší, než předchozí­
    if ( numbers[i] >= numbers[i - 1] ):

        # Pokud jde o první­ prvek v posloupnosti
        if ( currLen == 0 ):

            # Přičte jak aktiuální­, tak předchozí­ prvek posloupnosti
            currLen += 2;
            currSum += numbers[i-1] + numbers[i];

        else:

            # Přičte aktuální­ prvek
            currLen += 1;
            currSum += numbers[i];

    else:

        # Pokud je aktuální posloupnost delší, použijeme ji
        # Stejně tak, pokud je stejně dlouhá, ale má větší­ sumu        
        if ( ( prevLen < currLen) or ( ( prevLen == currLen ) and ( prevSum < currSum ) ) ):
        
            prevLen = currLen;
            prevSum = currSum;

        # Vyresetuje aktuální posloupnost
        currLen = 0;
        currSum = 0;

# Vypíše délku a na další řádek sumu delší/větší­ posloupnosti
if ( ( prevLen < currLen) or ( ( prevLen == currLen ) and ( prevSum < currSum ) ) ):
    print(currLen);
    print(currSum);
else:
    print(prevLen);
    print(prevSum);
