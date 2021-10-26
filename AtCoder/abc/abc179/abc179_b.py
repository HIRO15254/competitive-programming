N = int(input())
c = 0
for _ in range(N):
    a, b = map(int, input().split(" "))
    if a == b:
        c += 1
        if c >= 3:
            print("Yes")
            break
    else:
        c = 0
else:
    print("No")
