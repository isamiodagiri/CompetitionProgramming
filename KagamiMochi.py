a = int(input())#整数
li = []
ans = 1
for i in range(a):
    li.append(int(input()))

for i in range(a - 1):
    val = max(li)
    li.remove(val)
    ans += 1 if val > max(li) else 0
print(ans)