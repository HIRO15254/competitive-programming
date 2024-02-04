N = int(input())
A = map(int, input().split(" "))

ans = 0
maxdis = 0
dis = 0
pos = 0

for i in A:
    dis += i
    maxdis = max(maxdis, dis)
    ans = max(ans, pos + maxdis)
    pos += dis
print(ans)
