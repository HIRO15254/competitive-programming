import itertools
n = int(input())
k = int(input())
s = []
for _ in range(n):
    s.append(input())
ans = set()
for i in itertools.permutations(s, k):
    st = ""
    for j in i:
        st += j
    ans.add(st)
print(len(ans))
