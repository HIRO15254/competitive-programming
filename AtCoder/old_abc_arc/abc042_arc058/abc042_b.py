N, L = map(int, input().rstrip().split(" "))
A = []
for i in range(N):
    A.append(input())
A.sort()
print("".join(A))
