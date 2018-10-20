n = list(map(int,input().split()))
a = list(map(int,input().split()))
l = list(map(int,input().split()))
d = list(map(int,input().split()))
sum = 0
for i in l:
    if i in a:
        sum+=1
for i in d:
    if i in a:
        sum-=1
print(sum)
