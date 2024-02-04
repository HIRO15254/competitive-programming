komoji = "abcdefghijklmnopqrstuvwxyz"
s = input()
for i in range(25):
    if komoji[i] == s:
        print(komoji[i + 1])
