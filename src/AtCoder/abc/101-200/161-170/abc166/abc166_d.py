X = int(input())
A = [0] * 201
flag = True
for i in range(200):
    A[i] = i ** 5
for i in range(200):
    if(flag is False):
        break
    for i2 in range(i):
        if abs(X - A[i]) == A[i2]:
            if X - A[i] >= 0:
                print(str(i) + " " + str(-1 * i2))
            else:
                print(str(i) + " " + str(i2))
            flag = False
            break
