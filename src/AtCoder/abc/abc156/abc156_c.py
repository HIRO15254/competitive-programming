N = int(input())
X = list(map(int, input().rstrip().split(" ")))
ans = 0
ansb = 0
for i in range(100):
    ansb = 0
    for i2 in range(N):
        ansb += (X[i2] - i)**2
    if i == 0 or ans > ansb:
        ans = ansb
print(ans)
