def fact(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f
n = int(input())
for i in range(n):
    for j in range(i+1):
        l = int((fact(i))/(fact(j)*fact(i-j)))
        print(l,end = '',sep = ' ')
    print('\n')
