n, a, b = map(int, input().split())#複数

ans = 0
for i in range(n):
    s = str(i + 1)
    array = list(map(int, s))
    ans += i + 1 if a <= sum(array) and sum(array) <= b else 0

print(ans)