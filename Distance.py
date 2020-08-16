N, D = map(int, input().split())#複数

d = D ** 2
ans = 0

for i in range(N):
    X, Y = map(int, input().split())#複数
    if X ** 2 + Y ** 2 <= d:
        ans += 1


print(ans) 
