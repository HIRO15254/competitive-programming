N, K = map(int, input().split(" "))
R, S, P = map(int, input().split(" "))
T = input()
T += "q" * K
win = [True for i in range(N)]
for i in range(N):
    if T[i] == T[i + K]:
        if win[i]:
            win[i + K] = False
ans = 0
for i in range(N):
    if win[i]:
        if T[i] == "r":
            ans += P
        if T[i] == "s":
            ans += R
        if T[i] == "p":
            ans += S
print(ans)
