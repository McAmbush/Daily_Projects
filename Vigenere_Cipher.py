
print(100*'=')
print("Blaise Cipher".center(100,'-'))
print(100*'=')



li = []
n = int(input('1. Cipher\n2. Decipher\n'))
if n==1:
    str = input('Enter text to be encoded:\n')
    ky = input('\nEnter the key:\n')
    l = len(str)
    l2 = len(ky)
    ky = ky.lower()
    i=0
    j=0
    while i<l:
        ch = str[i]
        ch2 = ch.lower()
        n = ord(ch2)
        m = ord(ky[j])
        ch = str[i]
        n-=97
        m-=97
        sum = m+n
        if sum>=0 and sum<=25:
            if ch.islower():
                li.append(chr(97+sum))
            elif ch.isupper():
                d = chr(97+sum)
                d = d.upper()
                li.append(d)
            j+=1
        elif sum>25 and sum<=50:
            k = sum-26
            if ch.islower():
                li.append(chr(97+k))
            elif ch.isupper():
                d = chr(97+k)
                d = d.upper()
                li.append(d)
            j+=1
        else:
            li.append(chr(97+n))
        i+=1
        if j==(l2):
            j=0
    print('The Ciphered code is:\n')
    print(''.join(li),sep = '')
elif n==2:
    str = input('Enter text to be decoded:\n')
    ky = input('\nEnter the key:\n')
    ky = ky.lower()
    l = len(str)
    l2 = len(ky)
    i=0
    j=0
    while i<l:
            ch = str[i]
            ch2 = ch.lower()
            n = ord(ch2)
            m = ord(ky[j])
            n-=97
            m-=97
            sum = n-m
            if sum>=0 and sum<=25:
                if ch.islower():
                    li.append(chr(97+sum))
                elif ch.isupper():
                    d = chr(97+sum)
                    d = d.upper()
                    li.append(d)
                j+=1
            elif sum>=-25 and sum<0:
                k = sum+26
                if ch.islower():
                    li.append(chr(97+k))
                elif ch.isupper():
                    d = chr(97+k)
                    d = d.upper()
                    li.append(d)
                j+=1
            else:
                li.append(chr(n+97))
            i+=1
            if j==(l2):
                j=0
    print('The Deiphered code is:\n')
    print(''.join(li),sep = '')
