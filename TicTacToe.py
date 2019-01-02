r = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
end = False
def show(r):
    print('    ',r[0],'|','    ',r[1],'|','    ',r[2])
    print(24*'_')
    print('\n    ',r[3],'|','    ',r[4],'|','    ',r[5])
    print(24*'_')
    print('\n    ',r[6],'|','    ',r[7],'|','    ',r[8])
def box():
    n = int(input('Enter box number: '))
    if n in range(0,10):
        return n-1
    else:
        print('Invalid box number!')
def p1():
    print('Player 1s turn!')
    n = box()
    if r[n]=='X' or r[n]=='O':
        print('Box is occupied!')
        print('Enter another number!')
        p1()
    else:
        r[n] = 'O'
def p2():
    print('Player 2s turn!')
    n = box()
    if r[n]=='X' or r[n]=='O':
        print('Box is occupied!')
        print('Enter another number!')
        p1()
    else:
        r[n] = 'X'
def check():
    c = 0
    term = False
    for i in range(9):
        if r[i]=='X'or r[i]=='O':
            c+=1
    
 
    for i in range(7):
        if r[i]==r[i+1]==r[i+2]=='O':
            print('Player 1 wins!')
            end=True
        i+=3
    for i in range(7):
        if r[i]==r[i+1]==r[i+2]=='X':
            print('Player 2 wins!')
            end=True
        i+=3
    for i in range(3):
        if r[i]==r[i+3]==r[i+6]=='O':
            print('Player 1 wins!')
            end=True
    for i in range(3):
        if r[i]==r[i+3]==r[i+6]=='X':
            print('Player 2 wins!')
            end=True
    if r[0]==r[4]==r[8]=='O':
        print('Player 1 wins!')
        end=True
    if r[0]==r[4]==r[8]=='X':
        print('Player 2 wins!')
        end=True
    if r[2]==r[4]==r[6]=='O':
        print('Player 1 wins!')
        end=True
    if r[2]==r[4]==r[6]=='O':
        print('Player 2 wins!')
        end=True
    if c == 9:
        print('Game has ended! No winners!')
        end = True
    if term == True:
        print('Game has ended!\n No Winners!')
        end = True
while end==False:
    r1 = [1,2,3,4,5,6,7,8,9]
    check()
    show(r1)
    p1()
    show(r)
    check()
    p2()
    show(r)
