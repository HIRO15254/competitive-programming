N = int(input())
S1 = list(input())
S2 = list(input())
i = 0
ans = 1
lis = []
while i < N:
    if S1[i] == S2[i]:
        lis.append(0)
        if(i == 0):
            ans *= 3
        else:
            if lis[-2] == 0:
                ans *= 2
        i += 1
    else:
        lis.append(1)
        if(i == 0):
            ans *= 6
        else:
            if lis[-2] == 0:
                ans *= 2
            else:
                ans *= 3
        i += 2
    ans %= 10 ** 9 + 7
print(ans)
