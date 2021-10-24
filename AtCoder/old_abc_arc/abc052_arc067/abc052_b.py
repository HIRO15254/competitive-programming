_ = int(input())
N = 0
S = list(input())
ans = 0
for i in S:
    if i == "I":
        N += 1
    else:
        N -= 1
    if ans < N:
        ans = N
print(ans)
