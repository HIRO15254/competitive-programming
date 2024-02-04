N = int(input())
A = list(map(int, input().split()))

n = 6
ans = [0] * (10 ** n)
for i in A:
    ans[i] += 1
for i in range(n):
    for j in range(10 ** (n - i - 1)):
        for k in range(10 ** i):
            for l in range(9):
                ans[j * (10 ** (i + 1)) + ((l + 1) * (10 ** i)) + k] += ans[j * (10 ** (i + 1)) + (l * (10 ** i)) + k]
ret = 0
for i in A:
    ret += ans[999999 - i]
    if str(i).count("5") + str(i).count("6") + str(i).count("7") + str(i).count("8") + str(i).count("9") == 0:
        ret -= 1
print(ret // 2)