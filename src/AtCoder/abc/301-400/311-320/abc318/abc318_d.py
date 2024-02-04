from itertools import combinations

N = int(input())
D = []
for i in range(N - 1):
    D.append([0] * (i + 1) + list(map(int, input().split())))


def get_left_itel(n):
    left_item = []
    for i in range(N):
        if not n & (1 << i):
            left_item.append(i)
    return list(combinations(left_item, 2))


dp = [0] * (2 ** N)
for i in range(N // 2):
    for j in combinations(range(N), i * 2):
        j_val = 0
        for k in j:
            j_val += 2 ** k
        left_iter = get_left_itel(j_val)
        for left in left_iter:
            dp_index = j_val + 2 ** left[0] + 2 ** left[1]
            dp[dp_index] = max(dp[dp_index], dp[j_val] + D[left[0]][left[1]])
print(max(dp))
