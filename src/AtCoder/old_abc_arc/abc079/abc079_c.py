A = list(map(int, list(input())))
for i in range(8):
    a = A[0]
    ans_str = str(A[0])
    for j in range(3):
        if 1 & i >> j:
            a += A[j + 1]
            ans_str += "+"
        else:
            a -= A[j + 1]
            ans_str += "-"
        ans_str += str(A[j + 1])
    if a == 7:
        print(ans_str + "=7")
        break
