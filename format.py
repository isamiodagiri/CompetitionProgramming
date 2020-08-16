#文字入力系

import io
import sys

_INPUT = """\
2
1 2 3
aaa
"""
sys.stdin = io.StringIO(_INPUT)

#



# 入力系
a = input()#文字列
a = int(input())#整数
a, b = map(int, input().split())#複数
x = list(map(int, input().split()))#配列Int型
x = [list(map(int, input().split())) for i in range(3)]#複数（行）


#特殊入力　入力回数分
a = int(input())#整数
li = []

for i in range(a):
    li.append(list(map(int, input().split())))#配列Int型



# 出力系
print()#標準
print(x, y, z, sep="\n")#区切り

# ソート
sorted(list(map(int, input().split())))[::-1]#降順