N = int(input())
A = list(map(int, input().rstrip().split(" ")))
ave = 0
ans = 0
for i in A:
    ave += i
ave /= N
ave = (ave + 0.5) // 1
for i in A:
    ans += (i - ave) ** 2
print(int(ans))
