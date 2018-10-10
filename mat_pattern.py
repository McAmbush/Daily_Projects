li = list(map(int,input().split()))
n = li[0]
m = li[1]
l = int((n-1)/2)
i = 0
k = 1
q = int((m-3)/2)
j = q
x = int((m-7)/2)
while i<l:
    print(j*'-',k*'.|.',j*'-',sep='')
    i+=1
    j-=3
    k+=2
print(x*'-','WELCOME',x*'-',sep='')
l = int((n-1)/2)
i = 0
k = (n-2)
q = int((m-3)/2)
j = 3
while i<l:
    print(j*'-',k*'.|.',j*'-',sep = '')
    i+=1
    j+=3
    k-=2
    
