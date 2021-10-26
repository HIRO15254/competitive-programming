ans = []
for _ in range(2):
    li = []
    for _ in range(10):
        li.append(int(input()))
    li.sort(reverse=True)
    ans.append(li[0] + li[1] + li[2])
print(ans[0], ans[1])
