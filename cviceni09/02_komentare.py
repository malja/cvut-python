i = input()

STATE_NOT_STRING = 0
STATE_DOUBLE_QUOTE = 1
STATE_SIMPLE_QUOTE = 2
STATE_ERROR = -1
STATE_BACKSLASH = 3
STATE_COMMENT = 4

def stateMachine( line ):
    state = []
    state.append( STATE_NOT_STRING )

    for char in line:

        current = state[-1]

        if current == STATE_NOT_STRING:
            if char == "\"":
                print( char, end='')
                state.pop()
                state.append( STATE_DOUBLE_QUOTE )
            elif char == "\'":
                print( char, end='')
                state.pop()
                state.append( STATE_SIMPLE_QUOTE )
            elif char.isalpha() or char == "=":
                print(char, end='')
            elif char == "#":
                state.pop()
                state.append( STATE_COMMENT )

        elif current == STATE_DOUBLE_QUOTE:

            if char == "\\":
                state.append( STATE_BACKSLASH )
            elif char == "\"":
                state.pop()
                state.append(STATE_NOT_STRING)

            print( char, end='')
        
        elif current == STATE_SIMPLE_QUOTE:

            if char == "\\":
                state.append( STATE_BACKSLASH )
                
            elif char == "\'":
                state.pop()
                state.append( STATE_NOT_STRING )

            print( char, end='')
        
        elif current == STATE_BACKSLASH:
            state.pop()
            print(char, end='')
        
        elif current == STATE_COMMENT:
            if ( len(state) - 1 ) > 0:
                print()
                print("Špatný state")
            return

stateMachine( i )