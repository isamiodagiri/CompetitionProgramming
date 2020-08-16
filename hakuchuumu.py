S = input()#文字列

while len(S) > 0:
    count = len(S)

    if S.endswith("eraser"):
        S = S[:-6]
    elif S.endswith("erase"):
        S = S[:-5]
    if S.endswith("dreamer"):
        S = S[:-7]
    elif S.endswith("dream"):
        S = S[:-5]

    if count == len(S):
        break

T = "NO" if len(S) > 0 else "YES"

print(T)