N = int(input())
A = list(map(int, input().split()))
ans = 0
minus = 0
for i in A:
    if i < 0:
        minus += 1
if minus % 2 == 0:
    print(sum(map(abs, A)))
else:
    print(sum(map(abs, A)) - min(map(abs, A)) * 2)
