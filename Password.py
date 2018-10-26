import hashlib

def hashit(passw):
    hs = hashlib.sha256(passw.encode('utf-8'))
    hp = hs.hexdigest()
    return hp

def cipher(text):
    li = []
    str = text
    ky = 'alabama'
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
    s = ''.join(li)
    l = hashit(s)
    return l

print(80*'=')
print("PASSWORD ENCRYPTOR".center(80))
print(80*'=')





n = int(input('1. New Data\n2. Login\n'))
if n == 1:
    uid = input("Enter User ID\n")
    pwd = input("Enter Password\n")
    encr = cipher(pwd)
    f = open('idf.txt','w')
    f.write(uid)
    f.close()
    f2 = open('pwd.txt','w')
    f2.write(encr)
    f2.close()
elif n == 2:
    uid = input("Enter User ID\n")
    pwd = input("Enter Password\n")
    encr = cipher(pwd)
    f = open('idf.txt','r')
    u2 = f.read()
    f.close()
    f2 = open('pwd.txt','r')
    p2 = f2.read()
    f2.close()
    if u2 == uid and p2 == encr:
        print('You da master!')
    else:
        print('Dobby is a free elf!')
