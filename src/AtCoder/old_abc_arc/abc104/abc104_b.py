S = list(input())
if S[0] == "A" and S[2:-1].count("C") == 1:
    c = 0
    for i in S:
        if i != i.lower():
            c += 1
    if c == 2:
        print("AC")
    else:
        print("WA")
else:
    print("WA")
