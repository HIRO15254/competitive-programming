import itertools
A = list(map(int, input().split()))
ans = 10 ** 18
for i in itertools.permutations(range(3)):
    ans = min(ans, abs(A[i[0]] - A[i[1]]) + abs(A[i[1]] - A[i[2]]))
print(ans)
