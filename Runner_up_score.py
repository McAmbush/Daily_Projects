n = int(input('Enter no of inputs:  '))
li = list(map(int,input('Enter n inputs: ').split()))
l = []
for i in li:
    if i not in l:
        l.append(i)
big1 = l[0]
ln = len(l)
for i in range(1,ln):
    if l[i]>big1:
        big1 = l[i]
l.remove(big1)
if len(l) == 1:
    print(l[0])
else:
    big2 = l[0]
    ln2 = len(l)
    for i in range(1,ln2):
        if l [i]>big2:
            big2 = l[i]
print('The runner-up score is ',big2)