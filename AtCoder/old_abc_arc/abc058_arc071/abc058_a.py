A, B, C = map(int, input().rstrip().split(" "))
if B - A == C - B:
    print("YES")
else:
    print("NO")
