print(100*'=')
print('Caesar Cipher'.center(100,'-'))
print(100*'=')



l = []
choice = int(input('1. Cipher\n2. Decipher\n'))
if choice == 1:
        str = input('Enter text to be encoded:\n')
        ln = len(str)
        for i in range(ln):
            n = ord(str[i])
            if n>=97 and n<122:
                l.append(chr(n+1))
            elif n==122:
                l.append(chr(97))
            elif n>=65 and n<90:
                l.append(chr(n+1))
            elif n==90:
                l.append(chr(65))
            else:
                l.append(chr(n))
        print('The Ciphered code is:')
        print(''.join(l),sep = '')
if choice  == 2:
        str = input('Enter text to be decoded:\n')
        ln = len(str)
        for i in range(ln):
            n = ord(str[i])
            if n>97 and n<=122:
                l.append(chr(n-1))
            elif n==97:
                l.append(chr(122))
            elif n>65 and n<=90:
                l.append(chr(n-1))
            elif n==65:
                l.append(chr(90))
            else:
                l.append(chr(n))
        print('The Deciphered code is:')
        print(''.join(l),sep = '')            
