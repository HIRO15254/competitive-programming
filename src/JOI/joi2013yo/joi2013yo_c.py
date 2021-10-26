N = int(input())
S = list(input())
r = [0 for i in range(N)]
ans = 0
for p in range(N):
    I = list(input())
    for i in range(100):
        if r[p] == 1:
            break
        for j in range(50):
            for k in range(len(S)):
                if i + (j * k) >= len(I):
                    break
                elif I[i + (j * k)] != S[k]:
                    break
            else:
                ans += 1
                r[p] = 1
                break
print(ans)
