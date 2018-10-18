if __name__ == '__main__':
    s = input()
    alpha = -1
    for i in range(len(s)):
        if s[i].isalpha():
                alpha = 0
 
        num = -1
    for i in range(len(s)):
        if s[i].isdigit():
                num = 0
   
    lower = -1
    for i in range(len(s)):
        if s[i].islower():
                lower = 0
    
    upper = -1
    for i in range(len(s)):
        if s[i].isupper():
                upper = 0
   
    if alpha==0 or num==0:
        print('True')
    else:
        print('False')
    if alpha == 0:
        print('True')
    else:
        print('False')
    if num == 0:
        print('True')
    else:
        print('False')
    if lower == 0:
        print('True')
    else:
        print('False')
    if upper == 0:
        print('True')
    else:
        print('False')
