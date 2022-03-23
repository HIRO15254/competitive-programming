N = int(input())
left = list(range(2, 2 * N + 2))
print(1)
k = int(input())
while k != 0:
    left.remove(k)
    print(left[0])
    left.pop(0)
    k = int(input())
