a = int(input())
lis = list(map(int, input().split()))
flag = True
count = 0

while flag:
    for i in range(a):
        if lis[i] % 2 == 0:
            lis[i] = lis[i] / 2
        else:
            flag = False
            break
    count += 1 if flag else 0

print(count)