# 整数の入力
a, b = map(int, input().split())

ans = "Odd"

if a * b % 2 == 0:
    ans = "Even"
# 出力
print(ans)