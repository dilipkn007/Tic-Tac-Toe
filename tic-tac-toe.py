# q | w | e
#---+---+---
# a | s | d
#---+---+---
# z | x | c
theBoard={'q':'   ','w':'   ','e':'   ','a':'   ','s':'   ','d':'   ','z':'   ','x':'   ','c':'   '}
keyForSpaces={'q':' q ','w':' w ','e':' e ','a':' a ','s':' s ','d':' d ','z':' z ','x':' x ','c':' c '}
def printBoard(board):
    print(board['q']+'|'+board['w']+'|'+board['e'])
    print('---+---+---')
    print(board['a']+'|'+board['s']+'|'+board['d'])
    print('---+---+---')
    print(board['z']+'|'+board['x']+'|'+board['c'])
printBoard(theBoard)
turn='X'
while(True):
    print('Turn for '+turn+'. Move on which space?')
    move=input()
    try:    
        if theBoard[move]=='   ':
            theBoard[move]=' '+turn+' '
        else:
            print('Invalid')
            continue
    except KeyError:
        print("Invalid key chosed\nRefer to the key spaces")
        printBoard(keyForSpaces)
        continue
    printBoard(theBoard)
    if(theBoard['q']==theBoard['w']==theBoard['e'] and theBoard['e']!='   ')or(theBoard['a']==theBoard['s']==theBoard['d'] and theBoard['d']!='   ')or(theBoard['z']==theBoard['x']==theBoard['c']and theBoard['c']!='   ')or(theBoard['q']==theBoard['s']==theBoard['c']and theBoard['c']!='   ')or(theBoard['e']==theBoard['s']==theBoard['z']and theBoard['e']!='   ')or(theBoard['q']==theBoard['a']==theBoard['z'] and theBoard['z']!='   ')or(theBoard['w']==theBoard['s']==theBoard['x'] and theBoard['x']!='   ')or(theBoard['e']==theBoard['d']==theBoard['c'] and theBoard['e']!='   '):
        print(turn+" won!!\nCongradulations")
        choice=input("\nPress r for restart game or q to quit :")
        if(choice=='r' or choice=='R'):
            theBoard={'q':'   ','w':'   ','e':'   ','a':'   ','s':'   ','d':'   ','z':'   ','x':'   ','c':'   '}
            printBoard(theBoard)
            turn='X'
            i=0
            continue
        elif(choice=='q' or choice=='Q'):
            break
        else:
            print("Invalid Choice")
            continue
    if turn=='X':
        turn='0'
    else:
        turn='X'