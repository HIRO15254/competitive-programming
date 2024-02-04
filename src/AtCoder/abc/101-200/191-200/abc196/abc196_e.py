ma = 10**18
mi = -1 * 10**18
sa = 0
N = int(input())
for i in range(N):
    a, t = map(int, input().split(" "))

    if t == 1:
        sa += a

    if t == 2:
        if mi < a - sa:
            mi = a - sa
            if mi > ma:
                ma = mi

    if t == 3:
        if a - sa < ma:
            ma = a - sa
            if ma < mi:
                mi = ma

Q = int(input())
x = list(map(int, input().split(" ")))

for i in x:
    if mi > i:
        print(mi + sa)
    elif ma < i:
        print(ma + sa)
    else:
        print(i + sa)
