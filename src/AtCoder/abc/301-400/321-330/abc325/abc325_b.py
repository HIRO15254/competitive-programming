N = int(input())
W_count = [0] * 24
for i in range(N):
    W, X = map(int, input().split())
    W_count[X] += W
ans = sum(W_count[9:18])
# print(W_count)
ans_memo = ans
for i in range(24):
    ans_memo -= W_count[(i + 9) % 24]
    ans_memo += W_count[(i + 18) % 24]
    if ans_memo > ans:
        ans = ans_memo
print(ans)
