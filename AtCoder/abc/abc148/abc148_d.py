N = int(input())
A = list(map(int, input().split(" ")))
c = 1
for i in A:
    if i == c:
        c += 1
if c == 1:
    print(-1)
else:
    print(N - c + 1)
