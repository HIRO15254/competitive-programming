S = input()
Sa = S[0::2]
Sb = S[1::2]
if Sa.islower() and (len(S) == 1 or Sb.isupper()):
    print("Yes")
else:
    print("No")
