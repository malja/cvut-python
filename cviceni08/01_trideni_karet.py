import copy

cards = [[0, 'Q'], [2, '6'], [1, 'K'], 
         [1, '8'], [2, '10'], [2, '4'], 
         [3, '4'], [0, '4'], [1, '3'], 
         [2, '5'], [0, 'K'], [3, 'A'], 
         [1, 'J'], [0, '3'], [0, '9']]

def cardTypeAsInt( card ):

    if card[1].isdigit():
        return int(card[1])

    if card[1] == "J":
        return 11
    elif card[1] == "Q":
        return 12
    elif card[1] == "K":
        return 13
    else:
        return 14

def compareCards( card1, card2 ):

    print("porovnávám karty:", card1, card2)

    if (card1[0] == card2[0]):
        print("rovny")
        if ( cardTypeAsInt( card1 ) < cardTypeAsInt( card2 ) ):
            print("barva1")
            return True
        else:
            print("barva2")
            return False    
    else:
        print("else")
        return card1[0] < card2[0]

def bubbleSort( array, swap_fn ):

    sorted = copy.deepcopy(array)

    for i in range( len( sorted ) ):
        while( swap_fn( sorted[i], sorted[i-1] ) ):
                    tmp = sorted[i-1]
                    sorted[i-1] = sorted[i]
                    sorted[i] = tmp

    return sorted

print( cards )
print( bubbleSort( cards, compareCards) )



