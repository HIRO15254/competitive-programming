N, X = map(int, input().split(" "))
a = [1]
a2 = []
k = []
for i in range(N):
    A = list(map(int, input().split(" ")))
    for j in A[1:]:
        for k in a:
            a2.append(j * k)
    a = a2
    a2 = []
print(a.count(X))
