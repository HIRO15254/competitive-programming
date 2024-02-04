N, X, T = map(int, input().rstrip().split(" "))
ans = N // X
if N % X != 0:
    ans += 1
print(ans * T)
