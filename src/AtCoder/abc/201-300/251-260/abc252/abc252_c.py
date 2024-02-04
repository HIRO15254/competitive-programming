N = int(input())
S = []
for i in range(N):
    S.append(list(input()))
ans = 10 ** 18
for i in range(10):
    i_ans = 0
    t = [0] * 10
    for s in S:
        t[s.index(str(i))] += 1
    for j in range(10):
        i_ans = max(i_ans, (t[j] - 1) * 10 + j)
    ans = min(ans, i_ans)
print(ans)
