N = int(input())
A, B = map(int, input().split(" "))
C = int(input())
dol = A
cal = C
topping = []
for i in range(N):
    topping.append(int(input()))
topping.sort(reverse=True)
i = 0
while topping[i] / B > cal / dol:
    dol += B
    cal += topping[i]
    i += 1
print(int((cal / dol) // 1))
