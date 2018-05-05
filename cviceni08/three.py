import copy

raw_data = input()


def parseRawData( raw ):

    """
    Funkce načte řetězec, který rozparsuje tak, aby oddělila čísla a matematické symboly do samostatných prvků pole
    Parameter: raw(string) - Řetězec ke zpracování
    Returns: list
    """

    infix_form = []
    number = ""

    # Projde string po písmenech
    for char in raw:

        # Pokud to není číslo
        if not char.isdigit():

            # Číselník není prázdný, ukončili jsme právě běžící číslo
            if len( number ) > 0:
                # Přidáme ho celé do pole
                infix_form.append( number )
                number = ""

            # Mezery ignorujeme
            if char == " ":
                continue

            # Ostatní znaky přidáme
            else:
                infix_form.append( char )

        # Přidáme číslo do číselníku
        else:
            number += char

    # Pokud nám zbylo něco v číselníku, přidáme to
    if len( number ) > 0:
        infix_form.append( number )       
    
    return infix_form

def isOperator( char ):

    """
    Funkce vracející info o předaném operátoru nebo None
    Parameter: char(string) - Znak pro otestování na operand
    Returns: None nebo info z operators.
    """

    operators = [

        { 
            "name": "^",
            "precedence": 4,
            "associativity": "right",
            "type": "binary"
        },
        {
            "name": "*",
            "precedence": 3,
            "associativity": "left",
            "type": "binary"
        },
        {
            "name": "/",
            "precedence": 3,
            "associativity": "left",
            "type": "binary"
        },
        {
            "name": "+", 
            "precedence": 2,
            "associativity": "left",
            "type": "binary"
        },
        {
            "name": "-",
            "precedence": 2,
            "associativity": "left",
            "type": "binary"
        }
    ]

    for operator in operators:
        if operator["name"] == char:
            return operator

    return None

def shuntingYard( infix ):

    output = []
    operators = []

    # Projde všechny prvky z pole infix
    for token in infix:

        # Pokud jde o číslo
        if token.isdigit():

            # Před číslem nesmí být číslo
            if ( (shuntingYard.last == shuntingYard.NUMBER) or
                (shuntingYard.last == shuntingYard.CPARENTHASIS) ):
                return "ERROR"

            # Přidá se na pole pro výstup
            output.append( token )

            # Poslední bylo číslo
            shuntingYard.last = shuntingYard.NUMBER

            continue

        # Vrací None nebo odpovídající informace o operátoru
        operator = isOperator( token )
        if operator != None:

            if operator["name"] == "-":

                if  ( ( shuntingYard.last == shuntingYard.OPARENTHASIS) or
                    (shuntingYard.last == shuntingYard.NOTHING) or
                    (shuntingYard.last == shuntingYard.UOPERATOR) or
                    (shuntingYard.last == shuntingYard.BOPERATOR)):
                    
                    operator = {
                        "name": "u",
                        "precedence": 5,
                        "associativity": "left",
                        "type": "unary"
                    }
                
                    operators.append( operator )
                    shuntingYard.last = shuntingYard.UOPERATOR
                    continue

            else:
                # Unární operátor - může být jen před plusem či mínusem
                if ( shuntingYard.last == shuntingYard.UOPERATOR and ( operator["name"] != "+" or operator["name"] != "-" ) ):
                    return "ERROR"
                # Operátor nesmí být první, a musí před ním být číslo nebo závorky
                elif ( (shuntingYard.last == shuntingYard.BOPERATOR) or 
                        (shuntingYard.last == shuntingYard.OPARENTHASIS) or
                        (shuntingYard.last == shuntingYard.NOTHING) ):
                    return "ERROR"

            # Dokud na stacku jsou operátory, které mají vyšší prioritu než aktuální
            while   ( len( operators ) > 0 and (
                        ( (operator["associativity"] == "left") and (operator["precedence"] <= operators[-1]["precedence"]) ) or 
                        ( (operator["associativity"] == "right") and (operator["precedence"] < operators[-1]["precedence"]) )
                    ) ):

                # vloží se na výstup
                output.append( operators.pop()["name"] )

            # Vloží nový operátor na stack
            operators.append( operator )
            
            # Poslední byl binární/unární operátor
            shuntingYard.last = shuntingYard.BOPERATOR

            continue

        # Pokud je token otevírací závorka
        if token == "(":

            # Před závorkou může být cokoliv krom )
            if shuntingYard.last == shuntingYard.CPARENTHASIS:
                return "ERROR"

            # Přihodí závorku na stack
            operators.append( { "name":"(", "associativity": None, "precedence": -1 } )

            # POslední byla otevírací závorka
            shuntingYard.last = shuntingYard.OPARENTHASIS

            continue

        # Pokud je token uzavírací závorka
        if token == ")":

            # Před ) může být jen číslo nebo jiná )
            if ( (shuntingYard.last != shuntingYard.NUMBER) and
                (shuntingYard.last != shuntingYard.CPARENTHASIS) ):
                return "ERROR"

            # Pokud není na stacku žádná otevírací závorka
            if not { "name":"(", "associativity": None, "precedence": -1 } in operators:
                return "ERROR"

            # Dokud je něco na stacku
            while ( len( operators ) > 0 ):
                # a není to otevírací závorka
                if not operators[-1]["name"] == "(":
                    # přihodí to na výstup
                    output.append( operators.pop()["name"] )
                else:
                    # našli jsme závorku, jen pop ze stacku
                    operators.pop()
                    break
            
            # Poslední byla uzavírací závorka
            shuntingYard.last = shuntingYard.CPARENTHASIS

            continue

    # Pokud něco zbylo
    if len( operators ) > 0:
        # Projdeme to
        for operator in reversed( operators ):
            # Pokud jsou to závorky, je špatně ozávorkováno a končíme
            if operator["name"] == "(" or operator["name"] == ")":
                return "ERROR"
            else:
                # Jinak šup s tím na výstup
                output.append( operator["name"] )

    return output

shuntingYard.NUMBER = 0
shuntingYard.BOPERATOR = 1
shuntingYard.UOPERATOR = 2
shuntingYard.OPARENTHASIS = 3
shuntingYard.CPARENTHASIS = 4
shuntingYard.NOTHING = 5
shuntingYard.last = shuntingYard.NOTHING

def threeAddressCode( postfix_form ):

    if postfix_form == "ERROR":
        return "ERROR"

    # Obsahuje všechny tXX:=
    output = []

    length = len( postfix_form )
    i = 0
    counter = 1

    # Dokud postfix_form neobsahuje jen jeden prvek
    while length > 1:

        # Pokud nejde o číslo
        if not postfix_form[i].isdigit():

            # Pokud je to unární mínus
            if postfix_form[i] == "u":

                # A je z čeho brát data
                if (i > 0):

                    # Parametr
                    a = postfix_form[i-1]

                    # Uložení výstupu
                    output.append( "t" + str( counter ) + ":=0-" + a )

                    # A do rovnice pro další použití
                    postfix_form[i] = "t" + str(counter)

                    # Smaže z rovnice parametr
                    postfix_form.pop( i - 1)

                    # Aktualizuje počítadlo
                    i -= 1
                    length -= 1
                    counter += 1

                # Nejsou data, konec
                else:
                    print( postfix_form )
                    return "ERROR"


            
            # Pokud jde o jiný operand než unární mínus
            else:

                # A je z čeho brát data
                if (i > 1):

                    # Operand
                    op = postfix_form[i]
                
                    # Druhý parametr
                    b = postfix_form[i-1]
                    # První parametr
                    a = postfix_form[i-2]

                    # Vloží txx:= na výstup
                    output.append("t" + str( counter ) + ":=" + a + op + b)

                    # A do rovnice jen tXX
                    postfix_form[i] = "t" + str( counter )

                    # Smaže z rovnice druhý parametr
                    postfix_form.pop( i - 1 )
                    
                    # Aktualizuje počítadlo
                    i -= 1

                    # Smaže z rovnice druhý parametr
                    postfix_form.pop( i - 1 )

                    # Aktualizuje počítadlo
                    i -= 1
                    length -=2
                    counter += 1

                # Není z čeho brát data, konec
                else:
                    return "ERROR"

            # Šup na další prvek
            i += 1

        # Je to číslo, nezajámá nás
        else:
            i += 1

    return output

#############################################

# Získá data ve formě pole s jednotlivými tokeny
array = parseRawData( raw_data )

# Převede na postfixní formu
postfix = shuntingYard( array )

# Pokusí se o převod do TAC
three_addr = threeAddressCode( postfix )

# Pokud se vše povedlo, vypíšeme TAC
if three_addr != "ERROR":
    for tac in three_addr:
        print(tac)
else:
    print("ERROR")
    exit()
