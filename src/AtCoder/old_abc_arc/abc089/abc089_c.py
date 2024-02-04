import itertools
N = int(input())
ans = 0
march = [0] * 5
for i in range(N):
    S = input()
    if S[0] in "MARCH":
        march["MARCH".find(S[0])] += 1
for i in itertools.combinations(range(5), 3):
    ans += march[i[0]] * march[i[1]] * march[i[2]]
print(ans)
