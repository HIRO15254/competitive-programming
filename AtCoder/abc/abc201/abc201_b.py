N = int(input())
L = []
for i in range(N):
    S, T = input().split(" ")
    T = int(T)
    L.append([T, S])
L.sort(reverse=True)
print(L[1][1])
