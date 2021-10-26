X, Y, A, B, C = map(int, input().split(" "))

if ((A - 1) // Y + 1) + ((B - 1) // Y + 1) + ((C - 1) // Y + 1) <= X:
    print("Yes")
    exit()
elif ((A - 1) // X + 1) + ((B - 1) // X + 1) + ((C - 1) // X + 1) <= Y:
    print("Yes")
    exit()

elif ((A - 1) // Y + 1) < X and ((B - 1) // (X - ((A - 1) // Y + 1)) + 1) + ((C - 1) // (X - ((A - 1) // Y + 1)) + 1) <= Y:
    print("Yes")
    exit()
elif ((B - 1) // Y + 1) < X and ((A - 1) // (X - ((B - 1) // Y + 1)) + 1) + ((C - 1) // (X - ((B - 1) // Y + 1)) + 1) <= Y:
    print("Yes")
    exit()
elif ((C - 1) // Y + 1) < X and ((B - 1) // (X - ((C - 1) // Y + 1)) + 1) + ((A - 1) // (X - ((C - 1) // Y + 1)) + 1) <= Y:
    print("Yes")
    exit()

elif ((A - 1) // X + 1) < Y and ((B - 1) // (Y - ((A - 1) // X + 1)) + 1) + ((C - 1) // (Y - ((A - 1) // X + 1)) + 1) <= X:
    print("Yes")
    exit()
elif ((B - 1) // X + 1) < Y and ((A - 1) // (Y - ((B - 1) // X + 1)) + 1) + ((C - 1) // (Y - ((B - 1) // X + 1)) + 1) <= X:
    print("Yes")
    exit()
elif ((C - 1) // X + 1) < Y and ((B - 1) // (Y - ((C - 1) // X + 1)) + 1) + ((A - 1) // (Y - ((C - 1) // X + 1)) + 1) <= X:
    print("Yes")
    exit()
print("No")
