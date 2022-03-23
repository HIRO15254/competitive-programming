X = int(input())
if X % 10 != 0:
    X -= X % 10
print(X // 10)
