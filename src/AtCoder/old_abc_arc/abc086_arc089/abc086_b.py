a, b = input().split(" ")
N = int(a + b)
i = 0
while i ** 2 <= N:
    if N == i ** 2:
        print("Yes")
        exit()
    i += 1
print("No")
