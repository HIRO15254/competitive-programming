ans = set()
for a in range(1, 334):
    for b in range(1, 334):
        ans.add(3 * a + 4 * a * b + 3 * b)
N = int(input())
S = list(map(int, input().split(" ")))
ans2 = 0
for i in S:
    if i not in ans:
        ans2 += 1
print(ans2)
