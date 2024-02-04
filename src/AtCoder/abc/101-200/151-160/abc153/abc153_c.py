inp = input().rstrip().split(" ")
N = int(inp[0])
K = int(inp[1])
inp = input().rstrip().split(" ")
HP = [0 for i in range(N)]
for i in range(N):
    HP[i] = int(inp[i])
HP.sort()
HP.reverse()
ans = 0
for i in range(N):
    if i >= K:
        ans += HP[i]
print(ans)
