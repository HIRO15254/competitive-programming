A, B = input().rstrip().split(" ")
X, Y = map(int, input().rstrip().split(" "))
U = input()
if A == U:
    X -= 1
else:
    Y -= 1
print(str(X) + " " + str(Y))
