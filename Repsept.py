import io
import sys

_INPUT = """\
101
"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())
A = 7 % K 

for i in range(1, K + 1):
    if A % K == 0:
        print(i)
        exit()
    A = (10 * A + 7) % K
print(-1)