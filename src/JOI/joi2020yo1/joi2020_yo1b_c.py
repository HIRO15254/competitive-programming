S = [0 for i in range(101)]
_ = input()
A = list(map(int, input().rstrip().split(" ")))
ans = 0
for i in A:
    S[i] += 1
    if S[i] > ans:
        ans = S[i]
print(ans)
