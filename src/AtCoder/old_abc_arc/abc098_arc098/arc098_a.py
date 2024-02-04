N = int(input())
S = list(input())
ans_s = S[1:].count("E")
ans = ans_s
for leader in range(1, N):
    if S[leader] == "E":
        ans_s -= 1
    if S[leader - 1] == "W":
        ans_s += 1
    ans = min(ans_s, ans)
print(ans)
