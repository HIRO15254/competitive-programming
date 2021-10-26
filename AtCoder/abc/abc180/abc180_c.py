N = int(input())
ans = []
i = 1
while i ** 2 <= N:
    if N % i == 0:
        ans.append(i)
    i += 1

for i in ans:
    print(i)

ans.reverse()
for i in ans:
    if i ** 2 != N:
        print(N // i)
