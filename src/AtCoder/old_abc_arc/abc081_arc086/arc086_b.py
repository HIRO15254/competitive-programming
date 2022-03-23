N = int(input())
a = list(map(int, input().split(" ")))
ans = []
a_max = 0
a_min = 0
for i in a:
    a_max = max(i, a_max)
    a_min = min(i, a_min)
if abs(a_max) >= abs(a_min):
    j = a.index(a_max)
    for i in range(N):
        if a[i] != a_max:
            ans.append([j + 1, i + 1])
            a[i] += a_max
    for i in range(N - 1):
        if a[i] > a[i + 1]:
            ans.append([i + 1, i + 2])
            a[i + 1] += a[i]
else:
    j = a.index(a_min)
    for i in range(N):
        if a[i] != a_min:
            ans.append([j + 1, i + 1])
            a[i] += a_min
    for i in range(N - 1, 0, -1):
        if a[i - 1] > a[i]:
            ans.append([i + 1, i])
            a[i - 1] += a[i]
print(len(ans))
for i in ans:
    print(" ".join(map(str, i)))
