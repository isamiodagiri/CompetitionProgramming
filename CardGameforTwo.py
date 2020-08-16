a = int(input())#整数
x = sorted(list(map(int, input().split())))[::-1]
alice = 0    
bob = 0
for i in range(a):
    alice += x[i] if (i + 1) % 2 == 1 else 0
    bob += x[i] if (i + 1) % 2 == 0 else 0
ans = alice - bob
print(ans)