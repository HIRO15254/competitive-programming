N = int(input())
ans = []
for i in range(N):
    ans.append(["."] + list(input()) + ["."])
for i in range(N - 1):
    for j in range(N * 2 - 1):
        if ans[-1 * (i + 2)][j + 1] == "#":
            if "X" in ans[-1 * (i + 1)][j:j + 3]:
                ans[-1 * (i + 2)][j + 1] = "X"

for i in range(N):
    print("".join(ans[i][1:-1]))
