A, B = map(lambda x:int(x) - 1, input().split())
ans = []
for i in range(50):
    ans.append(["#" for _ in range(100)])
for i in range(50):
    ans.append(["." for _ in range(100)])
for i in range((A - 1) // 50 + 1):
    for j in range(min(A - 50 * i, 50)):
        ans[i * 2][j * 2] = "."
for i in range((B - 1) // 50 + 1):
    for j in range(min(B - 50 * i, 50)):
        ans[99 - i * 2][j * 2] = "#"
print(100, 100)
for i in range(100):
    print("".join(ans[i]))