A, B, C = map(int, input().rstrip().split(" "))
q = 0
for i in range(200):
    q += A
    if q % B == C:
        print("YES")
        break
    if i == 199:
        print("NO")
