N = int(input())
mat = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    for x in range(A, B):
        for y in range(C, D):
            mat[x][y] = 1
ans = 0
for i in range(100):
    ans += sum(mat[i])
print(ans)
