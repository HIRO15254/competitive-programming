N = int(input())
A = list(map(int, input().split()))

max_val = 0
ans = 0

val = 0

for i in range(2, 1000):
    val = 0
    for j in A:
        if j % i == 0:
            val += 1
    if val > max_val:
        ans = i
        max_val = val
print(ans)
