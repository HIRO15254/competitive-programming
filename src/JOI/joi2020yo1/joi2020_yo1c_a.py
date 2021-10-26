X, L, R = map(int, input().rstrip().split())
if L <= X <= R:
    print(X)
elif min(abs(X - L), abs(X - R)) == abs(X - L):
    print(L)
else:
    print(R)
