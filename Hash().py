n = int(input())
integer_list = list(map(int, input().split()))
l = tuple(integer_list)
print(hash(l))
