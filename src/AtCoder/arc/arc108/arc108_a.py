S, P = map(int, input().split(" "))
i = 1
ans = False
while i ** 2 <= P:
    if i * (S - i) == P:
        ans = True
        break
    i += 1
if ans:
    print("Yes")
else:
    print("No")
