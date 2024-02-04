N = int(input())
S = input()
if (S.count("T") > S.count("A")):
    print("T")
elif (S.count("T") < S.count("A")):
    print("A")
else:
    if (S[-1] == "A"):
        print("T")
    else:
        print("A")
