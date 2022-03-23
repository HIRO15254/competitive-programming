N, A, B = map(int, input().split(" "))
ans = 0
for i in range(1, N + 1):
    i_s = list(map(int, list(str(i))))
    if A <= sum(i_s) and sum(i_s) <= B:
        ans += i
print(ans)
