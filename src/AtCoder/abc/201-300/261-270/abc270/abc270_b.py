X, Y, Z = map(int, input().split())
if ((X * Y < 0) or (abs(X) < abs(Y))):
    print(abs(X))
elif ((Y * Z < 0) or (abs(Y) > abs(Z))):
    if (X * Z < 0):
        print(abs(X) + abs(Z) * 2)
    else:
        print(abs(X))
else:
    print(-1)
