N = int(input())
T = list(map(int, input().rstrip().split(" ")))
time = 0
for i in T:
    time += i
M = int(input())
for _ in range(M):
    P, X = map(int, input().rstrip().split(" "))
    print(X - T[P - 1] + time)
