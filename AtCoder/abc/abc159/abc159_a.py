A, B = map(int, input().rstrip().split(" "))
ans = int((A * (A - 1) / 2) + (B * (B - 1) / 2))
print(ans)
