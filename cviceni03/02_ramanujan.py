# Zadání:
#########
# Ramanujan (1887-1920) byl velmi zajímavý geniální indický matematik.
# Byl objeven prof. Hardym a pozván do Anglie. Zde onemocněl a když ho
# prof. Hardy navštívil v nemocnici, řekl mu, že za ním přijel taxíkem
# číslo XXXX. Ramanujan mu okamžitě odpověděl, že je to velmi zajímavé
# číslo, protože je to nejmenší číslo, které lze zapsat dvěma různými
# způsoby jako součet dvou krychlí (třetích mocnin přirozených čísel).
# Najděte čtyřciferné číslo taxíku XXXX.

maximum = 10000

# Hledám čtyři čísla splňující:
# a**3 + b**3 = c**3 + d**3
# Není nad for!

for a in range(1, maximum):

    a_cubed = a**3

    # Pokud samo a stačí na přesažení maxima, nemá cenu hledat dál
    if a_cubed >= maximum:
        break
    
    # Začíná se na a-čku, aby se zabránilo duplikátům
    for b in range( a, maximum):
        b_cubed = b**3

        # a**3 + b**3 musí být čtyřmístné
        if (b_cubed + a_cubed > maximum):
            break

        # Začíná se od a-čka, aby se zabránilo duplikátům
        for c in range( a+1, maximum ):
            c_cubed = c**3

            # C-čko nemůže být samo o sobě větší, než hodnoty a a b.
            if c_cubed > a_cubed + b_cubed:
                break

            # Začíná se od c-čka, aby se zabránilo duplikátům
            for d in range( c, maximum):
                d_cubed = d**3

                # Pokud je suma vyšší než na druhé straně, nemá cenu hledat dál
                if c_cubed + d_cubed > a_cubed + b_cubed:
                    break

                # Nalezli jsme, co hledáme
                if ( a_cubed + b_cubed == d_cubed + c_cubed):
                    # Výpis ve formátu:
                    # 1729 = 1^3 + 12^3 = 9^3 + 10^3
                    # Parametr sep="" nastavuje oddělovač mezi předchozími parametry, které se mají vypsat
                    print( a_cubed + b_cubed, " = ", a, "^3 + ", b, "^3 = ", c, "^3 + ", d, "^3", sep='' )
                    
                    # Pokud nechcete jen nejmenší číslo, stačí smazat exit
                    exit()