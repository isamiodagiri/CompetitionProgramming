S = str(input())

if S in 'RRR':
    print(3)
elif 'RR' in S:
    print(2)
elif 'R' in S:
    print(1)
else:
    print(0)