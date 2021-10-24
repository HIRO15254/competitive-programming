H, W = map(int, input().rstrip().split(" "))
N = int(input())
a = list(map(int, input().rstrip().split(" ")))
ans = [[0 for _ in range(W)]for _ in range(H)]
nowx = 0
nowy = 0
iki = True
for i in range(N):
    for j in range(a[i]):
        ans[nowy][nowx] = i + 1
        if iki:
            nowx += 1
            if nowx >= W:
                nowx = W - 1
                nowy += 1
                iki = False
        else:
            nowx -= 1
            if nowx < 0:
                nowx = 0
                nowy += 1
                iki = True
for i in range(H):
    print(" ".join(map(str, ans[i])))
