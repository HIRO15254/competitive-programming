X, Y, A, B = map(int, input().split(" "))
ans = 0
while X * (A - 1) <= B:
    if X * A < Y:
        X *= A
        ans += 1
    else:
        break
ans += (Y - X) // B
if (Y - X) % B == 0:
    ans -= 1
print(ans)
