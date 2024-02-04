N = int(input())
S = input()
S_1, S_2 = S.split("*")
if S_1.count("|") == 1 and S_2.count("|") == 1:
    print("in")
else:
    print("out")
