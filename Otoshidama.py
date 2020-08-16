A, T = map(int, input().split())

for i in range(A + 1):
    for j in range(A + 1):
        z = A - (j + i)
        if 1000 * z + 5000 * j + 10000 * i == T and z >= 0:
            print(i,j,z)
            exit(0)
print(-1,-1,-1)