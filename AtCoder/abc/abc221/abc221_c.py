import itertools
N = list(input())
N.sort()
ans = 0
for i in itertools.permutations(N):
    for j in range(1, len(N)):
        if i[0] != '0' and i[j] != '0':
            ans = max(ans, int("".join(i[:j])) * int("".join(i[j:])))
print(ans)
