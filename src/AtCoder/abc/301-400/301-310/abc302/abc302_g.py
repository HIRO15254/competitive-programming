import itertools

N = int(input())
A = list(map(int, input().split()))
A_s = sorted(A)

ans = 0
left = 0

c = [[0, 0, 0, 0] for _ in range(4)]
for i in range(N):
    if A[i] != A_s[i]:
        c[A[i] - 1][A_s[i] - 1] += 1
        left += 1

for i in itertools.permutations([0, 1, 2, 3], 2):
    k = min(c[i[0]][i[1]], c[i[1]][i[0]])
    ans += k
    c[i[0]][i[1]] -= k
    c[i[1]][i[0]] -= k
    
for i in itertools.permutations([0, 1, 2, 3], 3):
    k = min(c[i[0]][i[1]], c[i[1]][i[2]], c[i[2]][i[0]])
    ans += 2 * k
    c[i[0]][i[1]] -= k
    c[i[1]][i[2]] -= k
    c[i[2]][i[0]] -= k

for i in itertools.permutations([0, 1, 2, 3], 4):
    k = min(c[i[0]][i[1]], c[i[1]][i[2]], c[i[2]][i[3]], c[i[3]][i[0]])
    ans += 3 * k
    c[i[0]][i[1]] -= k
    c[i[1]][i[2]] -= k
    c[i[2]][i[3]] -= k
    c[i[3]][i[0]] -= k

print(ans)
