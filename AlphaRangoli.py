size = int(input())
n = int(size-1)
m = n*2
b = m
i = 0
while i<size:
    li = []
    li2 = []
    li3 = []
    for j in range(i+1):
        if j>0:
            li.append('-')
        li.append(chr(65+(size-j-1)))
    for k in range(i):
        if k>0:
            li2.append('-')
        li2.append(chr(65+(size-k-1)))
        li3 = li2[::-1]
    if i!=b:
        print(m*'-',''.join(li),'-',''.join(li3),m*'-',sep = '')
    else:
        p = (m-1)
        print(m*'-',''.join(li),'-',''.join(li3),p*'-',sep = '')
    m-=2
    i+=1

m = n
a = (n*2)
x = 0
li = []
li2 = []
for k in range(2,(m*2+2),2):
    li = []
    li2 = []
    li3 = []
    for j in range(m,x,-1):
        li.append(chr(65+j))
        li.append('-')
    x+=1
    li2 = li[::-1]
    li3 = li2[3:]
    if k!=(a):
        print(k*'-',''.join(li),''.join(li3),k*'-',sep = '')
    else:
        p = (k-1)
        print(k*'-',''.join(li),''.join(li3),p*'-',sep = '')
    
