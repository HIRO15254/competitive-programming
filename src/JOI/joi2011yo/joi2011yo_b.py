S = list(input())
N = int(input())
ans = 0
for _ in range(N):
    S2 = list(input())
    S2 += S2
    for i in range(len(S2)):
        if S2[i:i + len(S)] == S:
            ans += 1
            break
print(ans)
