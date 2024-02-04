S = list(input())
T = list(input())
ans = 10 ** 9
nowans = 0
for i in range(len(S) - len(T) + 1):
    nowans = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            nowans += 1
    ans = min(ans, nowans)
print(ans)
