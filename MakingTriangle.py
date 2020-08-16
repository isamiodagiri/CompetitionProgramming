a = int(input())#整数
x = list(map(int, input().split()))#配列Int型

x.sort()
ans = 0

for i in range(a):
    for j in range(i + 1, a):
        for k in range(j + 1, a):
            if x[k] < x[i] + x[j] and x[i] < x[j] < x[k]:
                ans += 1



            
print(ans)