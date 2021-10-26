N = int(input())
a = list(map(int, input().rstrip().split(" ")))
ans = [0] * (10 ** 5 + 3)
for i in a:
    ans[i + 2] += 1
    ans[i] += 1
    ans[i + 1] += 1
print(max(ans))
