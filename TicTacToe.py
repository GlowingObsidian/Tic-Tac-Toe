import random

def copy(array):
    array_copy=[[],[],[]]
    for i in range(0,3):
        for j in array[i]:
            array_copy[i].append(j)
    return array_copy

def draw_board(board):
    print()
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]=='-'):
                print(' ',end='')
            else:
                if(board[i][j]==1):
                    print('x',end='')
                else:
                    print('o',end='')
            
            if(j!=2):
                print('|',end='')
            else:
                print()
        if(i!=2):
            print('-----')

def turns_left(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]=='-'):
                return True
    return False

def win(board):
    if(board[0][0]!='-' and board[0][0]==board[0][1] and board[0][0]==board[0][2]):
        return board[0][0]
    elif(board[1][0]!='-' and board[1][0]==board[1][1] and board[1][0]==board[1][2]):
        return board[1][0]
    elif(board[2][0]!='-' and board[2][0]==board[2][1] and board[2][0]==board[2][2]):
        return board[2][0]
    elif(board[0][0]!='-' and board[0][0]==board[1][0] and board[0][0]==board[2][0]):
        return board[0][0]
    elif(board[0][1]!='-' and board[0][1]==board[1][1] and board[0][1]==board[2][1]):
        return board[0][1]
    elif(board[0][2]!='-' and board[0][2]==board[1][2] and board[0][2]==board[2][2]):
        return board[0][2]
    elif(board[0][0]!='-' and board[0][0]==board[1][1] and board[0][0]==board[2][2]):
        return board[0][0]
    elif(board[0][2]!='-' and board[0][2]==board[1][1] and board[0][2]==board[2][0]):
        return board[0][2]

def play(board,user,comp):
    comp_win_turns=0
    user_win=False
    comp_win_pos=0
    user_win_pos=0
    for i in range(0,3):
        for j in range(0,3):
            temp=copy(board)
            if(temp[i][j]=='-'):
                temp[i][j]=user
                if(win(temp)==user):
                    user_win_pos=(i*3)+j
                    user_win=True
                    break

    for i in range(0,3):
        for j in range(0,3):
            temp=copy(board)
            if(temp[i][j]=='-'):
                temp[i][j]=comp
                if(win(temp)==comp):
                    comp_win_pos=(i*3)+j
                    comp_win_turns=1
                else:
                    for k in range(0,3):
                        for l in range(0,3):
                            temp2=copy(temp)
                            if(temp2[k][l]=='-'):
                                temp2[k][l]=comp
                                if(win(temp2)==comp):
                                    if(comp_win_turns==0 or comp_win_turns==3):
                                        comp_win_pos=(i*3)+j
                                        comp_win_turns=2
                                else:
                                    for m in range(0,3):
                                        for n in range(0,3):
                                            temp3=copy(temp2)
                                            if(temp3[k][l]=='-'):
                                                temp3[k][l]==comp
                                                if(win(temp3)==comp):
                                                    if(comp_win_turns==0):
                                                        comp_win_pos=(i*3)+j
                                                        comp_win_turns=3

    if(user_win==True):
        if(comp_win_turns==1):
            return comp_win_pos
        else:
            return user_win_pos
    elif(user_win==False):
        if(comp_win_pos!=0):
            return comp_win_pos
        else:
            while(True):
                comp_win_pos=random.randint(0,8)
                if(board[comp_win_pos//3][comp_win_pos%3]=='-'):
                    break
            return comp_win_pos

def game():
    ch=str(input('Choose [X] or [O]: '))
    user=0
    comp=0
    if(ch=='X' or ch=='x'):
        user=1
        comp=0
    else:
        user=0
        comp=1

    board=[['-','-','-'],
           ['-','-','-'],
           ['-','-','-']]
    #play(board,2,user,comp)
    #print(win(board))
    #win_pattern(board)
    turn='user'
    if(user==0): turn='comp'
    while(turns_left(board)):
        if(win(board)!=None):
            break
        if(turn=='user'):
            position_user=int(input('Enter position: '))
            board[position_user//3][position_user%3]=user
            turn='comp'
        else:
            position_comp=play(board,user,comp)
            board[position_comp//3][position_comp%3]=comp
            turn='user'
        draw_board(board)

    print('Result: ',end='')
    if(win(board)!=None):
        if(win(board)==user):
            print('Player won')
        else:
            print('Computer Won')
    else:
        print('Draw')
    
    input('Enter any key to exit')
game()