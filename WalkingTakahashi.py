x, k, d = map(int, input().split())
x = abs(x)
res = x // d
if k <= res:
    print(abs(x - k * d))
elif (res + k) % 2 == 0:
    print(abs(x - res * d))
else:
    print(abs(x- (res + 1) * d))