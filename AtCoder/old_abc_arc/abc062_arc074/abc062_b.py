H, W = map(int, input().split())
ans = ["#" * (W + 2)]
for _ in range(H):
    ans.append("#" + input() + "#")
ans.append("#" * (W + 2))
for i in ans:
    print(i)
